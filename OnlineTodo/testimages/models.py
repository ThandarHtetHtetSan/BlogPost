from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):

    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)
    image=models.ImageField(blank=True,)

def __str__(self):
    return self.titlep



class PostImages(models.Model):
    post=models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
    images=models.ImageField(upload_to="images")

def __str__(self):
    return self.post.title