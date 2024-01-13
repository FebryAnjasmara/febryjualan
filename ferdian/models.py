from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

# Create your models here.

# Tabel Kategori

class Kategori(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=False)
    aktif = models.BooleanField(default= True)
    banner_satu = models.ImageField(upload_to='gambar/banner', verbose_name="Gambar (575 x 200 pixel)", blank=True, null=True)
    # banner_satu = ResizedImageField(size=[575, 200], 
    #                                 quality=80, crop=['middle', 'center'] , 
    #                                 upload_to='gambar/banner', blank=True, 
    #                                 null=True, 
    #                                 verbose_name="Gambar (575 x 200 pixel)")
    banner_dua = models.ImageField(upload_to='gambar/banner', verbose_name="Gambar (575 x 200 pixel)", blank=False, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    class Meta:
        verbose_name_plural ="Data Kategori"
    def __str__(self):
        return f"Kategori: {self.nama}, aktif: {self.aktif}"
    
    @property
    def get_produk(self):
        return Produk.objects.filter(kategori__slug=self.slug)


    

# Tabel Kategori End


# Tabel Produk
class Produk(models.Model):
    KETERANGAN=(
        ('Baru', 'Baru'),
        ('Lama' , 'Lama'),
        )
    kategori = models.ForeignKey(Kategori, null=True, blank=True, 
                                 related_name="produks", on_delete=models.SET_NULL)
    nama_produk = models.CharField(max_length=200, blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar/banner', verbose_name="Gambar (270 x 250 pixel)", blank=False, null=True)
    gambar_satu = models.ImageField(upload_to='gambar/banner', verbose_name="Gambar 1 (270 x 250 pixel)", blank=True, null=True)
    gambar_dua = models.ImageField(upload_to='gambar/banner', verbose_name="Gambar 2 (270 x 250 pixel)", blank=True, null=True)
    gambar_tiga = models.ImageField(upload_to='gambar/banner', verbose_name="Gambar 3 (270 x 250 pixel)", blank=True, null=True)
    gambar_empat = models.ImageField(upload_to='gambar/banner', verbose_name="Gambar 4 (270 x 250 pixel)", blank=True, null=True)
    gambar_lima= models.ImageField(upload_to='gambar/banner', verbose_name="Gambar 5 (270 x 250 pixel)", blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    # keterangan = models.TextField(max_length=200, blank=True, null=True)
    keterangan = RichTextField(blank=True, null=True)
    harga = models.PositiveIntegerField(blank=True, null=True)
    no_whatsup = models.PositiveBigIntegerField(blank=True, null=True,)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    diskon = models.IntegerField(default=0, verbose_name="diskon (%)", blank=True, null=True)
    dibeli = models.IntegerField(default=0, blank=True, null=True)
    aktif = models.BooleanField(default=False)
    keterangan_barang = models.CharField(max_length=200, null=True, 
                                         choices=KETERANGAN)
    
    @property
    def setelah_diskon(self):
        if self.diskon == 0 :
            nilai_diskon = self.harga
        else:
            jml = self.diskon / 100
            nilai_diskon = self.harga - (jml * self.harga)
        return nilai_diskon
    
    class Meta:
        verbose_name_plural ="Data Produk"
    def __str__(self):
        return self.nama_produk


# Tabel Produk End


# Tabel Slide

class Slide(models.Model):
    class Meta:
        verbose_name_plural ="Data Slide"
    teks_awal = models.CharField(max_length=200, blank=True, null=True)
    teks_dua = models.CharField(max_length=200, blank=True, null=True)
    teks_tiga = models.CharField(max_length=200, blank=True, null=True)
    gambar_slide = models.ImageField(upload_to='gambar/slide', verbose_name="Gambar Slide (475 x 880 pixel)", blank=False, null=True)
    aktif = models.BooleanField(default=True)

# Tabel Slide End


# Tabel Kontak

class Kontak(models.Model):
    class Meta:
        verbose_name_plural ="Data Kontak"
    nama = models.CharField(max_length=200, blank=False, null=True)
    no_whatsup = models.PositiveBigIntegerField(blank=True, null=True,)
    email = models.EmailField(max_length=200,blank=False, null=True)
    subject = models.CharField(max_length=200, blank=False, null=True)
    isi = models.TextField(max_length=200, blank=False, null=True)

# Tabel Kontak End


# Tabel Profil

class Profil(models.Model):
    class Meta:
        verbose_name_plural ="Data Profil"
    nama = models.CharField(max_length=200, blank=False, null=True)
    keterangan = RichTextField(blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar/profil', blank=False, 
                               null=True, verbose_name="Gambar (1920 x 1200 pixel)")
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)

# Tabel Profil End


# Tabel Statis

class Statis(models.Model):
    class Meta:
        verbose_name_plural ="Data Statis"
    alamat_kami = models.TextField(max_length=200, blank=False, null=True)
    telpon = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)

# Tabel Statis End
    
# Tabel ChatID

class ChatID(models.Model):
    chatid = models.CharField(max_length=200, blank=False, null=True)
    nama = models.CharField(max_length=200, blank=False, null=True)
    aktif = models.BooleanField(default= True)
    
    class Meta:
        verbose_name_plural ="Data Chat ID"

# Tabel ChatID End