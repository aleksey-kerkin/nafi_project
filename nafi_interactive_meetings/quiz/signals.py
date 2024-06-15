from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Question, Answer


@receiver(post_save, sender=Question)
def create_answers(sender, instance, **kwargs):
    Answer.objects.create(
        answer=instance.correct_answer,
        is_correct=True,
        user=instance.user,
        question=instance
    )

    for k, v in instance.__dict__.items():
        if 'wrong_answer' in k and v:
            Answer.objects.create(
                answer=v,
                is_correct=False,
                user=instance.user,
                question=instance
            )
