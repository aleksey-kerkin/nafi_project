from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        # Получаем текст вопроса из запроса
        question_text = self.request.data.get("question_text")

        # Сохраняем вопрос с обработанным текстом
        serializer.save(user=self.request.user, question_text=question_text)
