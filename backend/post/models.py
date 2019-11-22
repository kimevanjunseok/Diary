from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    imgfile = ProcessedImageField(
        upload_to = 'blog/post',
		format = 'JPEG',					
		options = {'quality': 100})