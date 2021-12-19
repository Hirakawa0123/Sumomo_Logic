from django.db import models

class Pdf(models.Model):
    class Meta:
        db_table = 'pdf'
    file_name = models.CharField(verbose_name='ファイル名',max_length=70)
    content = models.TextField(verbose_name='コンテンツ',max_length=20000,blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

class Search(models.Model):
    class Meta:
        db_table = 'search'
    search_name = models.CharField(verbose_name='search_name',max_length=70)
    file_path = models.CharField(verbose_name='file_path',max_length=70)
    search_query = models.TextField(verbose_name='search_query',max_length=1000,blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search_name