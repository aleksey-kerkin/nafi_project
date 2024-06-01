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
    title = models.CharField('Название викторины', max_length=128)
    description = models.TextField('Описание викторины')
    banner = models.ImageField('Баннер викторины', upload_to=user_directory_path)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'

    def __str__(self):
        return f'{self.user} -> {self.title}'


class Question(models.Model):
    title = models.CharField('Название вопроса', max_length=256)
    image = models.ImageField('Изображение', upload_to=user_directory_path)

    correct_answer = models.CharField('Правильный ответ', max_length=128, blank=False, null=True)
    wrong_answer_1 = models.CharField('Ошибочный ответ', max_length=128, blank=False, null=True)
    wrong_answer_2 = models.CharField('Ошибочный ответ', max_length=128)
    wrong_answer_3 = models.CharField('Ошибочный ответ', max_length=128)
    wrong_answer_4 = models.CharField('Ошибочный ответ', max_length=128)
    wrong_answer_5 = models.CharField('Ошибочный ответ', max_length=128)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Викторина')

    class Meta:
        verbose_name = 'Вопрос викторины'
        verbose_name_plural = 'Вопросы викторины'

    def __str__(self):
        return f'{self.quiz} -> {self.title}'
