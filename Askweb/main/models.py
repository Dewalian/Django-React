from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    ask_post = models.CharField(max_length=300)

    def __str__(self):
        return self.title
