from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    """Сущность мероприятия"""
    title = models.CharField('Название продукта', max_length=128, blank=False)
    start_date = models.DateTimeField('Дата/время проведения', blank=True)
    pdf = models.ImageField(upload_to='media/pdfs')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title
