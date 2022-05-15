from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from boardapp.models import PostCategory


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
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='category', null=False)


    def __str__(self):
        return str(self.post_id) + ' - ' + str(self.category) + ' - ' + str(self.post_title)