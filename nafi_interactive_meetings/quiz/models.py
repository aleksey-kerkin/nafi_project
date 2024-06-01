from uuid import uuid1

from django.db import models
from django.conf import settings

from screencast.models import Event


# Create your models here.
def user_directory_path(instance, filename):
    extension = filename.split('.')[-1]
    name = uuid1().hex
    filename = name + '.' + extension
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Quiz(models.Model):
    title = models.TextField('Название викторины', max_length=128)
    description = models.TextField('Описание викторины', max_length=512)
    banner = models.ImageField('Баннер викторины', upload_to=user_directory_path)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие', blank=True, null=True)

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'

    def __str__(self):
        return f'{self.user} -> {self.title}'


class Question(models.Model):
    title = models.TextField('Название вопроса', max_length=256)
    frame = models.ImageField('Изображение', upload_to=user_directory_path)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Викторина', blank=True, null=True)

    class Meta:
        verbose_name = 'Вопрос викторины'
        verbose_name_plural = 'Вопросы викторины'

    def __str__(self):
        return f'{self.quiz} -> {self.title}'
