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
    """Сущность викторины"""
    title = models.CharField('Название викторины', max_length=128)
    description = models.TextField('Описание викторины', blank=True)
    banner = models.ImageField('Баннер викторины', upload_to=user_directory_path, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'

    def __str__(self):
        return f'{self.user} -> {self.title}'


class Question(models.Model):
    """Сущность вопроса для викторины"""
    title = models.CharField('Вопрос викторины', max_length=256)
    image = models.ImageField('Изображение', upload_to=user_directory_path, blank=True)

    correct_answer = models.CharField('Правильный ответ', max_length=128)
    wrong_answer_1 = models.CharField('Ошибочный ответ', max_length=128)
    wrong_answer_2 = models.CharField('Ошибочный ответ', max_length=128, blank=True)
    wrong_answer_3 = models.CharField('Ошибочный ответ', max_length=128, blank=True)
    wrong_answer_4 = models.CharField('Ошибочный ответ', max_length=128, blank=True)
    wrong_answer_5 = models.CharField('Ошибочный ответ', max_length=128, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Викторина')

    class Meta:
        verbose_name = 'Вопрос викторины'
        verbose_name_plural = 'Вопросы викторины'

    def __str__(self):
        return f'{self.quiz} -> {self.title}'


class Answer(models.Model):
    """Сущность варианта ответа для викторины (для хранения ссылок на участников)"""
    answer = models.CharField('Ответ на вопрос', max_length=128)
    is_correct = models.BooleanField('Верный')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос викторины')
    # users = models.ManyToManyField('EventUser', blank=True, verbose_name='Ответившие') # - тут должны быть ссылки на тех, кто выбрал этот вариант
