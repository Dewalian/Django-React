from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.question_view, name="question_view"),
    path("create/", views.question_create, name="question_create"),
    path("update/<int:id>", views.question_update, name="question_update"),
    path("delete/<int:id>", views.question_delete, name="question_delete")
]