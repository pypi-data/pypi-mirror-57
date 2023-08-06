from django.contrib.auth import get_user_model
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=120, unique=True)
    users = models.ManyToManyField(get_user_model(), related_name='users', blank=True)
    mods = models.ManyToManyField(get_user_model(), related_name='mods', blank=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='messages')
    deleted = models.BooleanField(default=False)
    message = models.TextField()
