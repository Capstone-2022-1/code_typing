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
        return str(self.practice_id) + ' - ' + str(self.code_language) + ' - ' + str(self.practice_chnum)
