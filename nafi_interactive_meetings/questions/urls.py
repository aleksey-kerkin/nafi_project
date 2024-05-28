from django.urls import path
from .views import QuestionAPIView, QuestionDetailAPIView


urlpatterns = [
    path("", QuestionAPIView.as_view(), name="question-list"),
    path("<int:pk>", QuestionDetailAPIView.as_view(), name="question"),
]
