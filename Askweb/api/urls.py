from django.urls import path
from . import views

urlpatterns = [
    path("user/<int:id>", views.user_api, name="user_api"),
    path("question/<int:id>", views.question_api, name="question_api")
]