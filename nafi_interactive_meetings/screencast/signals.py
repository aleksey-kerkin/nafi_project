from time import sleep
from pdf2image import convert_from_path

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Event, Slide



@receiver(post_save, sender=Event)
def add_to_group(sender, instance, **kwargs):
    print('!!! SIGNAL WAS WORKED !!!')
    print('!!! SIGNAL WAS WORKED !!!')
    print('!!! SIGNAL WAS WORKED !!!')
    # https://pypi.org/project/pdf2image/
    path_2_file = str(settings.MEDIA_ROOT) + '/' + str(instance.pdf)
    images = convert_from_path(path_2_file, 300)  # тут нужно как-то сам файл выдернуть
    # sleep(10)
    for i, image in enumerate(images):
        Slide.objects.create(
            title=i,
            jpeg=image,
            time=None,
            event=instance
        )
