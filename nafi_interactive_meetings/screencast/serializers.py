from rest_framework import serializers

from .models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = "__all__"

