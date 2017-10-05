from rest_framework import viewsets
from rooms.permissions import IsOwnerOrReadOnly
from rooms.models import Room, Message
from rooms.serializers import RoomSerializer, MessagesSerializer

import logging
log = logging.getLogger('django')


class RoomsViewSet(viewsets.ModelViewSet):
    """
    View for `create`, `delete`, `retrieve`, and `update` of
    Rooms model
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        log.info('Perform create object {}'.format(Room.name))
        serializer.save()


class MessageViewSet(viewsets.ModelViewSet):
    """
    View for `create`, `delete`, `retrieve`, and `update` of
    Message model
    """
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer

#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()
