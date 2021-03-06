from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Upractice(models.Model):
    upractice_id = models.AutoField(primary_key=True)
    upractice_title = models.CharField(max_length=32, null=False)
    upractice_content = models.TextField(null=False)
    upractice_result = models.TextField(null=False)
    upractice_chnum = models.IntegerField(null=False)
    writer = models.ForeignKey(User,on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.upractice_id) + ' - ' + str(self.upractice_title) + ' - ' + str(self.upractice_chnum) + ' - ' + str(self.writer)
