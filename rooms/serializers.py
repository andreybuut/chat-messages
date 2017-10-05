from django.contrib.auth.models import User
from rest_framework import serializers
from rooms.models import Room, Message


class MessagesSerializer(serializers.ModelSerializer):
    """
    Serialize Message model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = (
            'text',
            'owner',
            'url',
            'room'
        )


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Room model with nested Message model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    room = serializers.HyperlinkedRelatedField(
        view_name='message-detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Room
        fields = (
            'name',
            'owner',
            'url',
            'room',
        )
