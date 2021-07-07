from django.contrib.auth.models import User
from main.models import Question
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import QuestionSerializer, UserSerializer

# Create your views here.

@api_view(["GET"])
def user_api(request, id):
    model_data = User.objects.get(id=id)
    serializer = UserSerializer(model_data)
    return Response(serializer.data)

@api_view(["GET", "POST", "PUT", "DELETE"])
def question_api(request, id):
    model_data = Question.objects.get(id=id)
    if request.method == "GET":
        serializer = QuestionSerializer(model_data)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = QuestionSerializer(model_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        model_data.delete()
        model_data.save()
        return Response("item has been deleted")

