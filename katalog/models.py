from django.db import models

class KatalogBarang(models.Model):
    nama_barang = models.CharField(max_length=255)
    harga_barang = models.BigIntegerField()
    stok_barang = models.IntegerField()
    deskripsi = models.TextField()
    rating = models.IntegerField()
    url_barang = models.URLField()
