from django.db import models

# Create your models here.

class Pekerjaan(models.Model):
    nama = models.CharField(max_length=100)
    motto = models.TextField(max_length=200)

    def __str__(self):
        return self.nama