from django.db import models
from ferdian.models import Produk

# Create your models here.

# Tabel transaksi


class Transaksi(models.Model):
    class Meta:
        verbose_name_plural = "Data Transaksi"
    Status = (
        ('Baru', 'Baru'),
        ('Lunas', 'Lunas'),
    )
    no_transaksi = models.CharField(max_length=200, blank=False, null=True)
    nama_depan = models.CharField(max_length=200, blank=False, null=True)
    nama_belakang = models.CharField(max_length=200, blank=False, null=True)
    alamat = models.TextField(max_length=200, blank=False, null=True)
    provinsi = models.CharField(max_length=200, blank=False, null=True)
    kabupaten = models.CharField(max_length=200, blank=False, null=True)
    kecamatan = models.CharField(max_length=200, blank=False, null=True)
    kode_post = models.CharField(max_length=200, blank=False, null=True)
    email = models.CharField(max_length=200, blank=False, null=True)
    whatsapp = models.CharField(max_length=200, blank=False, null=True)
    total_transaksi = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=200, default="Baru", blank=True,
                              null=True, choices=Status)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tanggal_kirim = models.DateTimeField(auto_now_add=False, null=True, blank=False)

# Tabel transaksi End


# Tabel Detail Transaksi

class DetailTransaksi(models.Model):
    class Meta:
        verbose_name_plural = "Data Detail Transaksi"
    no_transaksi = models.CharField(max_length=200, blank=False, null=True)
    produk = models.ForeignKey(Produk, null=True, on_delete=models.SET_NULL)
    jumlah = models.IntegerField(blank=True, null=True)

# Tabel Detail Transaksi End