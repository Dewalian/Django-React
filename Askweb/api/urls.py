from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_overview, name="api_overview"),
    path("view/", views.all_view, name="all_view"),
    path("view/<int:id>/", views.question_view, name="question_view"),
    path("userview/<int:id>/", views.user_questions_view, name="user_question_view"),
    path("create/", views.question_create, name="question_create"),
    path("update/<int:id>/", views.question_update, name="question_update"),
    path("delete/<int:id>/", views.question_delete, name="question_delete")
]