from django.db import models

class Pdf(models.Model):
    file_name = models.CharField(max_length=70)

    def __str__(self):
        return self.file_name