from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.QuestionAll.as_view(), name="question_all"),
    path("<int:id>/", views.QuestionAPI.as_view(), name="question_api")
]

urlpatterns = format_suffix_patterns(urlpatterns)