from pdf2image import convert_from_path
from uuid import uuid1

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Event, Slide


@receiver(post_save, sender=Event)
def create_slides(sender, instance, **kwargs):
    """Функция разбивает презентацию пользователя на отдельные объекты слайдов."""
    # https://pypi.org/project/pdf2image/
    if instance.pdf and not instance.pdf_uploaded:
        path_2_file = str(settings.MEDIA_ROOT) + '/' + str(instance.pdf)
        images = convert_from_path(path_2_file, 300)
        for i, image in enumerate(images, 1):
            file_name = f'user_{instance.user.pk}/{uuid1().hex}.jpg'
            image.save(f'media/{file_name}')
            Slide.objects.create(
                title=i,
                jpeg=file_name,
                scheduled_time='00:05:00',
                time_spent='00:05:00',
                order=i,
                user=instance.user,
                event=instance
            )
        instance.pdf_uploaded = True
        instance.save()


@receiver(post_save, sender=Slide)
def set_order(sender, instance, **kwargs):
    """Функция переписывает порядковые номера слайдов по количеству слайдов."""
    event_id = instance.event
    all_slides = Slide.objects.filter(event=event_id).order_by('order')
    for n, v in enumerate(all_slides, 1):
        Slide.objects.filter(pk=v.id).update(order=n)
