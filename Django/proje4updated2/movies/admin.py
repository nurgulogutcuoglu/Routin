from django.contrib import admin

from .models import Yonetmen, Film, Oyuncu


# Eğer daha önce düz register ettiysek silip bunu yazalım:
@admin.register(Yonetmen)
class YonetmenAdmin(admin.ModelAdmin):
    fields = ['isim', 'biyografi', 'fotograf']  # fotoğraf alanını admin paneline zorla ekliyoruz


admin.site.register(Film)
admin.site.register(Oyuncu)
