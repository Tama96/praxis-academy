from django.db import models

# Create your models here.

class Sukucadang (models.Model):
    tanggal = models.CharField(max_length=100)
    jenis = models.CharField(max_length=100)
    kendaraan = models.CharField(max_length=100)
    jumlah = models.CharField(max_length=100)
    class Meta:
        db_table = "sukucadang"

        