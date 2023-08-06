from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_control, cache_page
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chat.models import Room, Message
from chat.serializers import RoomSerializer, MessageModelSerializer


def index_vue(request):
    return render(request, 'index.html', {})


@cache_control(max_age=3600, public=True)
@cache_page(60 * 60)
def service_worker(request):
    return FileResponse(
        open(settings.DIST_ROOT + "/service-worker.js", "rb"),
        content_type="application/javascript",
    )


@cache_control(max_age=3600, public=True)
@cache_page(60 * 60)
def manifest_json(request):
    return FileResponse(
        open(settings.DIST_ROOT + "/manifest.json", "rb"), content_type="application/json",
    )


@cache_control(max_age=3600, public=True)
@cache_page(60 * 60)
def precache_manifest(request, hash):
    try:
        with open(
            settings.DIST_ROOT + "/precache-manifest.{0}.js".format(hash), "rb"
        ) as file:
            response = FileResponse(
                file.read().decode(), content_type="application/javascript"
            )
    except FileNotFoundError:
        raise Http404()
    return response


class ApiStatusView(generics.RetrieveAPIView):
    permission_classes = (
        IsAuthenticated,
    )  # checks if user is authenticated to view the model objects

    def get_queryset(self):
        return Room.objects.filter(public=True)

    def get(self, request, *args, **kwargs):  # GET request handler for the model
        queryset = self.get_queryset()
        serializer = RoomSerializer(queryset, many=True)
        data = {'user': request.user.username, 'rooms': serializer.data}
        return Response(data)


class ChatRoomView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Room.objects.filter(public=True)

    def get(self, request, *args, **kwargs):  # GET request handler for the model
        queryset = self.get_queryset()
        room = get_object_or_404(queryset.filter(name=kwargs.get('room')))
        serializer = MessageModelSerializer(room.messages, many=True)
        return Response(serializer.data)
