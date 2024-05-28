from pdf2image import convert_from_path
from uuid import uuid1

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Event, Slide


@receiver(post_save, sender=Event)
def add_to_group(sender, instance, **kwargs):
    # https://pypi.org/project/pdf2image/
    path_2_file = str(settings.MEDIA_ROOT) + '/' + str(instance.pdf)
    images = convert_from_path(path_2_file, 300)
    for i, image in enumerate(images, 1):
        file_name = f'user_{instance.user.pk}/{uuid1().hex}.jpg'
        image.save(f'media/{file_name}')
        Slide.objects.create(
            title=i,
            time=5,
            jpeg=file_name,
            user=instance.user,
            event=instance
        )
