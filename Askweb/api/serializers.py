from django.contrib.auth.models import User
from main.serializers import QuestionSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True, source="question_set")
    
    class Meta:
        model = User 
        fields = ["id", "username", "email", "password", "question"]
        extra_kwargs = {"password": {"write_only": True}}


