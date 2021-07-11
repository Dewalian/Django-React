from main.models import Question
from django.contrib.auth.models import User
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "user", "title", "ask_post"]

class UserSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True, source="question_set")
    

    class Meta:
        model = User 
        fields = ["id", "username", "email", "question"]
