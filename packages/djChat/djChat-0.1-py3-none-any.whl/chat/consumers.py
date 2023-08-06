import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.utils import timezone

from .models import Room, Message
from .serializers import MessageSerializer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    room = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

    @database_sync_to_async
    def _get_room(self, user):
        room = Room.objects.get(name=self.room_name)
        if room.public:
            return room
        elif user in room.users or user in room.mods:
            return room

    async def connect(self):
        if not self.scope['user'].is_authenticated:
            return
        self.room = await self._get_room(self.scope['user'])
        if self.room:
            # Join room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)

            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def _save_message(self, message):
        Message.objects.create(
            room=self.room,
            date=message.get('date'),
            user=self.scope['user'],
            message=message.get('message'),
        )

    async def receive_json(self, content, **kwargs):
        """Receive message from WebSocket"""
        if not self.scope['user'] and self.scope['user'].username != content.user:
            return
        m = MessageSerializer(
            data={
                'user': self.scope['user'].username,
                'message': content['message'],
                'date': timezone.now(),
            }
        )

        if m.is_valid():
            # Save message
            await self._save_message(m.validated_data)
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': m.validated_data['message'],
                    'user': m.validated_data['user'],
                    'date': str(m.validated_data['date']),
                },
            )

    async def chat_message(self, event):
        """Receive message from room group"""
        user = event['user']
        message = event['message']
        date = event['date']

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {'user': user, 'message': message, 'date': date}, default=str
            )
        )
