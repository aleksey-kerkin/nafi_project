from django.urls import path, include
from rest_framework import routers
from .views import SlideListByEvent, EventViewSet

event_router = routers.SimpleRouter()
event_router.register(r'events', EventViewSet)
slide_router = routers.SimpleRouter()
slide_router.register(r'slides', EventViewSet)

urlpatterns = [
    path('', include(event_router.urls)),
    path('', include(slide_router.urls)),
    path('events/<int:event>/slides/', SlideListByEvent.as_view()),
]
