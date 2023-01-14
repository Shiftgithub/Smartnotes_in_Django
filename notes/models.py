from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="notes")

class Demos(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)