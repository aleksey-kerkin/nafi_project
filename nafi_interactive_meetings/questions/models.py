from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """Сущность вопроса"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, verbose_name="Отвечен")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"Вопрос от {self.user.username}: {self.question_text[:20]}"
