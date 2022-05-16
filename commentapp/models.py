from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from postapp.models import Post


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_content = models.TextField(null=False)
    comment_wdate = models.DateTimeField(auto_now_add=True)
    comment_mdate = models.DateTimeField(auto_now=True)
    like_num = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='comment')