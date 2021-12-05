from django.db import models

class Pdf(models.Model):
    class Meta:
        db_table = 'pdf'
    file_name = models.CharField(max_length=70)
    content = models.TextField(max_length=2000,blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

class Post(models.Model):
    """投稿モデル"""
    class Meta:
        db_table = 'post'
    title = models.CharField(verbose_name='タイトル', max_length=10)
    comment = models.CharField(verbose_name='コメント', max_length=100)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    def __str__(self):
        return self.title + ',' + self.comment