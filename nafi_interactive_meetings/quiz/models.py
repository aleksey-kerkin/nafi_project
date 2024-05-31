from django.contrib.auth.models import User
from django.db import models

from django.conf import settings


# Create your models here.
class Quiz(models.Model):
    name = models.TextField('Название викторины', max_length=128)
    description = models.TextField('Описание', max_length=512)
    banner = models.ImageField(
        upload_to=None,
        height_field=600,
        width_field=800,
        verbose_name='Баннер викторины'
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_c = models.DateTimeField(auto_now_add=True)
    date_u = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.TextField('Название вопроса', max_length=256)
    frame = models.ImageField(
        upload_to=None,
        height_field=600,
        width_field=800,
        verbose_name='Изображение'
    )
    answers = {}

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_c = models.DateTimeField(auto_now_add=True)
    date_u = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Вопрос викторины'
        verbose_name_plural = 'Вопросы викторины'

    def __str__(self):
        return self.name
