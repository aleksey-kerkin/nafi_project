from django.db import models
from django.contrib.auth.models import User

from pdf2image import convert_from_path


# Create your models here.
class Event(models.Model):
    """Сущность мероприятия"""
    title = models.CharField('Название мероприятия', max_length=128, blank=False)
    start_date = models.DateTimeField('Дата/время проведения', blank=True)
    pdf = models.ImageField('Презентация в PDF', upload_to='media/pdfs')
    current_slide = models.IntegerField(default=0)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    # slides = models.ForeignKey('Slide', on_delete=models.CASCADE, verbose_name='Слайды')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title

    def add_slides(self):
        """Метод разбивает файл PDF на слайды."""
        # https://pypi.org/project/pdf2image/
        images = convert_from_path(self.pdf, 300)  # тут нужно как-то сам файл выдернуть
        for i, image in enumerate(images):
            slide = Slide.objects.create(i, image)
            slide.save()


class Slide(models.Model):
    """Сущность слайда/блока/темы"""
    title = models.CharField('Название/номер слайда', max_length=128, blank=False)
    jpeg = models.ImageField('Слайд в JPEG', upload_to='media/jpgs')
    time = models.TimeField('Время на блок')

    event = models.ForeignKey(Event, blank=False, on_delete=models.CASCADE, verbose_name='Слайд')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.title
