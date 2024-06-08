from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Question, Answer


@receiver(post_save, sender=Question)
def create_answers(sender, instance, **kwargs):
    # доделать, когда доделаю модели
    Answer.objects.create(
        answer=instance.correct_answer,
        is_correct=True,
        user=instance.user,
        question=instance
    )

    # answer_dict = {}
    # for i in range(1, 6):
    #     answer_dict[f'wrong_answer_{i}'] = isinstance.__dict__.
