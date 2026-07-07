from django.db import models

class Yazı(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    kategori = models.CharField(max_length=100)
    # Yeni eklediğimiz resim alanı. Resimleri 'blog_gorselleri' klasörüne kaydedecek.
    # blank=True, null=True sayesinde görsel yüklemek zorunlu olmayacak, boş da bırakılabilecek.
    gorsel = models.ImageField(upload_to='blog_gorselleri/', blank=True, null=True)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik

