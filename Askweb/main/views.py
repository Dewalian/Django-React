from main.models import Question
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import QuestionSerializer
from django.http import Http404

class QuestionAll(APIView):
    def get(self, request, format=None):
        model_data = Question.objects.all()
        serializer = QuestionSerializer(model_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionAPI(APIView):
    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except:
            raise Http404
    
    def get(self, request, id, format=None):
        model_data = self.get_object(id)
        serializer = QuestionSerializer(model_data)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        model_data = self.get_object(id)
        serializer = QuestionSerializer(model_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model_data = self.get_object(id)
        model_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)