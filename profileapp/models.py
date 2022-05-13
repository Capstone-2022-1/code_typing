from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    #OneToOne() field는 장고에서 제공해주는 field 중 하나인데, profile과 user객체를 하나씩 연결해줌
    #upload_to는 전에 만들었던 settings.py 안에 media/profile에 저장이 됨.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    m_emoticon = models.ImageField(upload_to='profile/', null=True)
    user_nick = models.CharField(max_length=20, unique=True, null=True)