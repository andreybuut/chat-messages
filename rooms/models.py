from django.db import models
from model_utils.models import TimeStampedModel


class Message(TimeStampedModel):
    """
    Model for manage messages
    """
    text = models.CharField(max_length=120)
    #owner = models.ForeignKey('Account')
    room = models.ForeignKey('Room', related_name='room')

    def __str__(self):
        return self.text


class Account(models.Model):
    """
    Model for save user profile information.
    """
    username = models.CharField(max_length=50)


class Room(TimeStampedModel):
    """
    Model for save room, and messages
    """
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name
