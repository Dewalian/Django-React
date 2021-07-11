from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username", db_column="user", null=True)
    title = models.CharField(max_length=20)
    ask_post = models.TextField(max_length=600)

    def __str__(self):
        return self.title
