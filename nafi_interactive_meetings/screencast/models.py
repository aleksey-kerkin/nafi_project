from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    """Сущность мероприятия"""
    title = models.CharField('Название мероприятия', max_length=128, blank=False)
    start_date = models.DateTimeField('Дата/время проведения', blank=True)
    pdf = models.ImageField('Презентация в PDF', upload_to='media/pdfs')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title


class Element(models.Model):
    """Сущность слайда/блока/темы"""
    title = models.CharField('Название/номер слайда', max_length=128, blank=False)
    jpeg = models.ImageField('Слайд в JPEG', upload_to='media/pdfs')
    time = models.TimeField('Время на блок')

    event = models.ForeignKey(Event, blank=False, on_delete=models.CASCADE, verbose_name='Слайд')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.title
