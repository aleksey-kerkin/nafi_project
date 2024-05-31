from django.db import models
from auth_system.models import User

from uuid import uuid1


# Create your models here.
def user_directory_path(instance, filename):
    extension = filename.split('.')[-1]
    name = uuid1().hex
    filename = name + '.' + extension
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Event(models.Model):
    """Сущность мероприятия"""
    title = models.CharField('Название мероприятия', max_length=128, blank=False)
    start_date = models.DateTimeField('Дата/время проведения', blank=True)
    pdf = models.FileField('Презентация в PDF', upload_to=user_directory_path)
    current_slide = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.user} -> {self.title}'


class Slide(models.Model):
    """Сущность слайда/блока/темы"""
    title = models.CharField('Название/номер слайда', max_length=128, blank=False)
    jpeg = models.FileField('Слайд в JPEG', upload_to=user_directory_path)
    time = models.IntegerField('Время на блок, сек')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    event = models.ForeignKey(Event, blank=False, on_delete=models.CASCADE, verbose_name='Мероприятие')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return f'{self.event} -> {self.title}'
