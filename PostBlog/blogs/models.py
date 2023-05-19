from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS=((0,"Draft"),
        (1,"Publish"),
        (2,"Edit"))
class Post(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=200)
    content=models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_post')
    updated_on=models.DateTimeField(auto_now=True)
    created_on=models.DateTimeField(auto_now_add=True)
    thumnail=models.ImageField(default="Some string",upload_to="images",blank=True)
    status=models.IntegerField(choices=STATUS, default=1)
class Meta:
    ordering=['-created_on']
def __str__(self):
    return self.title

class PostImage(models.Model):
    post=models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
    images=models.ImageField(upload_to="images")

def __str__(self):
    return self.post.title


