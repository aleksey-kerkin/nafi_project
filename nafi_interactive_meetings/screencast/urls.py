from django.urls import path
from .views import EventAPIView, SlideAPIView, SlideListByEvent

urlpatterns = [
    path('events/', EventAPIView.as_view()),
    path('slides/', SlideAPIView.as_view()),
    path('events/<int:event>/slides/', SlideListByEvent.as_view()),
]
