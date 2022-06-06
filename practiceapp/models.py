from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=32, null=False)

    def __str__(self):
        return str(self.language_id) + ' - ' + str(self.language)


class Practice(models.Model):
    practice_id = models.AutoField(primary_key=True)
    code_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_code', null=False)
    code_content = models.TextField(null=False)
    code_result = models.TextField(null=False)
    practice_chnum = models.IntegerField(null=False)
    code_source = models.CharField(max_length=256,null=True)

    def __str__(self):
        return str(self.practice_id)



class Presult(models.Model):
    presult_id = models.AutoField(primary_key=True)
    presult_accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    presult_speed = models.IntegerField(null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    presult_time = models.IntegerField(null=False)
    presult_false_num = models.IntegerField(null=False)
    presult_summary = models.TextField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    practice_id = models.ForeignKey(Practice, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.presult_id) + ' - ' + str(self.user_id)
