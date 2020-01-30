from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    header = models.CharField(max_length=30)
    content = models.TextField(max_length=3000)
    image = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(blank=True)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='article')

    def __str__(self):
        return self.header


class Comment(models.Model):
    header = models.CharField(max_length=30)
    content = models.CharField(max_length=280)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        to=Article, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header
