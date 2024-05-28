from django.urls import path
from .views import EventAPIView, SlideAPIView

urlpatterns = [
    path('events/', EventAPIView.as_view()),
    path('events/<int:pk>/', EventAPIView.as_view()),
    path('slides/', SlideAPIView.as_view()),
    path('slides/<int:pk>/', SlideAPIView.as_view()),
]
