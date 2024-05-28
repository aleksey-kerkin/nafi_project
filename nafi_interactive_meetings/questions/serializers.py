from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "owner", "question_text", "pub_date", "completed"]
        read_only_fields = ["id", "pub_date"]
