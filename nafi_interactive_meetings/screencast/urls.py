from django.urls import path, include
from rest_framework import routers
from .views import SlideListByEvent, EventViewSet, SlideViewSet

router = routers.SimpleRouter()
router.register(r'events', EventViewSet)
router.register(r'slides', SlideViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('events/<int:event>/slides/', SlideListByEvent.as_view()),

]
