from django.db import models
from django.urls import reverse

# Create your models here.

class signup(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    password = models.CharField(max_length=19,default="password")

    def get_absolute_url(self):
        return reverse("signup:signup-detail",kwargs ={"id": self.id})
