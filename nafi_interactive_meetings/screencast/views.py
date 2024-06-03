from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
class EventAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)


class SlideAPIView(generics.ListCreateAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)
