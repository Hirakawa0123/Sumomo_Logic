from django.db import models

class Pdf(models.Model):
    file_name = models.CharField(max_length=70)
    content = models.TextField(max_length=2000,blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name