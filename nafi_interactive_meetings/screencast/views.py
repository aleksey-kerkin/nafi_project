from rest_framework import generics, viewsets
from .models import Event, Slide
from .serializers import EventSerializer, SlideSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = (
        Event.objects.all()
    )  # почему-то ругается без него, хотя по инструкции должно без него работать
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        if user.id is None:
            return None
        elif user.is_staff or user.is_superuser:
            return Event.objects.all()
        else:
            return Event.objects.filter(user=user)


class SlideViewSet(viewsets.ModelViewSet):
    queryset = (
        Slide.objects.all()
    )  # почему-то ругается без него, хотя по инструкции должно без него работать
    serializer_class = SlideSerializer

    def get_queryset(self):
        user = self.request.user
        if user.id is None:
            return None
        else:
            return Slide.objects.filter(user=user)


class SlideListByEvent(generics.ListAPIView):
    serializer_class = SlideSerializer

    def get_queryset(self):
        user = self.request.user
        if user.id is None:
            event_id = self.kwargs["event"]
            return Slide.objects.filter(event=event_id).order_by("order")
        elif user.is_staff or user.is_superuser:
            event_id = self.kwargs["event"]
            return Slide.objects.filter(event=event_id).order_by("order")
        else:
            event_id = self.kwargs["event"]
            return Slide.objects.filter(user=user, event=event_id).order_by("order")
