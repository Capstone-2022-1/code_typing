from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)

    post_title = models.CharField(max_length=256,null=False)
    image = models.ImageField(upload_to='post/', null=False)
    post_content = models.TextField(null=False)
    post_viewnum = models.IntegerField(default=0)
    like_num = models.IntegerField(default=0)
    post_wdate = models.DateTimeField(auto_now_add=True)
    post_mdate = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', null=False)