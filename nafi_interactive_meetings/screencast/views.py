from rest_framework import generics, viewsets
from .models import Event, Slide
from .serializers import EventSerializer, SlideSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()  # почему-то ругается без него, хотя по инструкции должно без него работать
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)


class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all()  # почему-то ругается без него, хотя по инструкции должно без него работать
    serializer_class = SlideSerializer

    def get_queryset(self):
        user = self.request.user
        return Slide.objects.filter(user=user)


class SlideListByEvent(generics.ListAPIView):
    serializer_class = SlideSerializer

    def get_queryset(self):
        user = self.request.user
        event_id = self.kwargs['event']
        return Slide.objects.filter(user=user, event=event_id)
