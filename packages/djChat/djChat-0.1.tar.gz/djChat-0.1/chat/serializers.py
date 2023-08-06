from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Room, Message


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class MessageSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    user = serializers.CharField(max_length=62)
    message = serializers.CharField(max_length=300)


class MessageModelSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['date', 'user', 'message']
