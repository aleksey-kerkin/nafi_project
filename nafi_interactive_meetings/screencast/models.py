from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

from uuid import uuid1


def user_directory_path(instance, filename):
    extension = filename.split('.')[-1]
    name = uuid1().hex
    filename = name + '.' + extension
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Event(models.Model):
    """Сущность мероприятия"""
    title = models.CharField('Название мероприятия', max_length=128, blank=False)
    start_date = models.DateTimeField('Дата/время проведения', blank=True)
    pdf = models.FileField(
        'Презентация в PDF',
        upload_to=user_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        blank=True,
    )
    pdf_uploaded = models.BooleanField('Презентация уже добавлена', default=False)
    current_slide = models.IntegerField('Текущий слайд', default=1)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.user} -> {self.title}'


class Slide(models.Model):
    """Сущность слайда/блока/темы"""
    title = models.CharField('Название/номер слайда', max_length=128, blank=False)
    jpeg = models.FileField('Слайд в JPEG', upload_to=user_directory_path, blank=True)
    data = models.TextField('Информация', blank=True)
    scheduled_time = models.TimeField('Запланированное время на блок', default='00:05:00', blank=True)
    time_spent = models.TimeField('Потраченное время на блок', default='00:00:00', blank=True)
    order = models.PositiveIntegerField('Порядковый номер слайда', blank=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    event = models.ForeignKey(Event, blank=False, on_delete=models.CASCADE, verbose_name='Мероприятие')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        # ordering = ('order',)

    def __str__(self):
        return f'{self.event} -> {self.title}'

    def save(self, *args, **kwargs):
        if self.order:
            if Slide.objects.filter(event=self.event, order=self.order).exists():
                Slide.objects.filter(event=self.event, order__gte=self.order).exclude(pk=self.pk).update(
                    order=models.F('order') + 1)
        super().save(*args, **kwargs)
