from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
class EventAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)


class SlideAPIView(generics.ListCreateAPIView):
    serializer_class = SlideSerializer

    def get_queryset(self):
        user = self.request.user
        return Slide.objects.filter(user=user)


class SlideListByEvent(generics.ListAPIView):
    serializer_class = SlideSerializer

    def get_queryset(self):
        user = self.request.user
        event_id = self.kwargs['event']  # получаем ID события из URL
        return Slide.objects.filter(user=user, event=event_id)
