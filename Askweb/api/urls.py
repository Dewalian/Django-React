from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.user_api, name="user_api"),
]