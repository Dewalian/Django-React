from django.contrib.auth.models import User
from main.models import Question
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import QuestionSerializer

# Create your views here.

@api_view(["GET"])
def question_view(request, id):
    user = User.objects.get(id=id)
    model_data = user.question_set.all()
    serializer = QuestionSerializer(model_data, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def question_create(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def question_update(request, id):
    model_data = Question.objects.get(id=id)
    serializer = QuestionSerializer(instance=model_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def question_delete(request, id):
    model_data = Question.objects.get(id=id)
    model_data.delete()
    return Response("item deleted")
