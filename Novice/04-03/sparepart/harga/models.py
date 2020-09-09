from django.db import models

# Create your models here.

class Harga (models.Model):
    sparepart = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    harga = models.CharField(max_length=200)
    class Meta:
        db_table = "harga"