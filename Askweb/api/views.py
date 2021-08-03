from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import UserSerializer
from rest_framework.authentication import BasicAuthentication
from . auth import CsrfExemptSessionAuthentication

class UserAPI(APIView):
    def get(self, request, id, format=None):
        model_data = User.objects.get(id=id)
        serializer = UserSerializer(model_data)
        return Response(serializer.data)

class UserAll(APIView):
    def get(self, request, format=None):
        model_data = User.objects.all()
        serializer = UserSerializer(model_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
