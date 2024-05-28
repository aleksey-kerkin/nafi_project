from rest_framework import serializers
from .models import Question
from .parsers import PlainTextParser


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "user", "question_text", "pub_date", "completed"]
        read_only_fields = ["id", "user", "pub_date"]
        parser_classes = [PlainTextParser]
