from rest_framework import generics, viewsets
from .models import Event, Slide
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, SlideSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Event.objects.all()
        return Event.objects.filter(user=user)


class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Slide.objects.all()
        return Slide.objects.filter(user=user)


class SlideListByEvent(generics.ListAPIView):
    serializer_class = SlideSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        user = self.request.user  # сейчас можно смотреть только свои созданные слайды, позже чужие по приглашению
        event = self.kwargs["event"]
        if user.is_staff:
            return Slide.objects.filter(event=event).order_by("order")
        return Slide.objects.filter(user=user, event=event).order_by("order")
