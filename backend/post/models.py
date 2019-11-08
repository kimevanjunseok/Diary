from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    photo = models.ImageField(blank=True)