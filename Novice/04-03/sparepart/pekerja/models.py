from django.db import models

# Create your models here.

class Pekerja (models.Model):
    nik = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    class Meta:
        db_table = "pekerja"