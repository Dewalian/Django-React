from django.contrib.auth.models import User
from main.models import Question
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import QuestionSerializer, UserSerializer

# Create your views here.

@api_view(["GET"])
def user_api(request):
    model_data = User.objects.all()
    serializer = UserSerializer(model_data, many=True)
    return Response(serializer.data)

    