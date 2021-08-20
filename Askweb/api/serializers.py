from django.contrib.auth.models import User
from main.serializers import QuestionSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True, source="question_set")
    
    class Meta:
        model = User 
        fields = ["id", "username", "email", "password", "question"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            username = validated_data["username"],
            email = validated_data["email"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
