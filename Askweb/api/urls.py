from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.user_all, name="user_all"),
    path("question/", views.question_all, name="question_all"),
    path("user/<int:id>", views.user_api, name="user_api"),
    path("question/<int:id>", views.question_api, name="question_api")
]