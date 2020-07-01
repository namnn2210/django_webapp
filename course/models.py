from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=8)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
