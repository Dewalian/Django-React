from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("<str:username>/", views.UserAPI.as_view(), name="user_api"),
    path("", views.UserAll.as_view(), name="user_all"),
    path("logout/blacklist/", views.BlackListToken.as_view(), name="blacklist")
]

urlpatterns = format_suffix_patterns(urlpatterns)