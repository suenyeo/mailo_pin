from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project')
    description = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateTimeField(auto_now=True)