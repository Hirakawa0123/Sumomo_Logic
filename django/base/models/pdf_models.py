from django.db import models

class Pdf(models.Model):
    class Meta:
        db_table = 'pdf'
    file_name = models.CharField(verbose_name='ファイル名',max_length=70)
    content = models.TextField(verbose_name='コンテンツ',max_length=20000,blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name