from rest_framework import generics
from .models import Event, Slide
from .serializers import EventSerializer, SlideSerializer


# Create your views here.
class EventAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SlideAPIView(generics.ListCreateAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
