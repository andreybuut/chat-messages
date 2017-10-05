from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rooms.views import RoomsViewSet, MessageViewSet

router = DefaultRouter()

router.register(r'rooms', RoomsViewSet, base_name='room')
router.register(r'message', MessageViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

]