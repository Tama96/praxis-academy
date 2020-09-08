from django.db import models

# Create your models here.

class Sukucadang (models.Model):
    tanggal = models.CharField(max_length=100)
    jenis = models.CharField(max_length=100)
    kendaraan = models.CharField(max_length=100)
    jumlah = models.CharField(max_length=100)
    class Meta:
        db_table = "sukucadang"

class Pekerja (models.Model):
    nik = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    class Meta:
        db_table = "pekerja"

class Harga (models.Model):
    sparepart = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    harga = models.CharField(max_length=200)
    class Meta:
        db_table = "harga"