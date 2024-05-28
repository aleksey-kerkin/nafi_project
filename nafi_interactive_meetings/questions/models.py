from django.db import models
from screencast.models import Event


class Question(models.Model):
    """
    Сущность вопроса.
    """

    owner = models.CharField(
        default="Без имени", help_text="Напишите имя", verbose_name="Имя", max_length=65
    )
    question_text = models.CharField(
        help_text="Задайте вопрос.", null=False, blank=False, verbose_name="Вопрос", max_length=200
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, verbose_name="Отвечен")
    event = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Мероприятие"
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"Вопрос от {self.owner}: {self.question_text[:20]}"
