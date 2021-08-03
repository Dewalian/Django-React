from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("<int:id>/", views.UserAPI.as_view(), name="user_api"),
    path("", views.UserAll.as_view(), name="user_all"),
]

urlpatterns = format_suffix_patterns(urlpatterns)