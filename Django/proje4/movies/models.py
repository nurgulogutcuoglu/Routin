import re
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


def validate_no_digits(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("Bu alan sayı/rakam içeremez.")


def validate_letters_only(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("Bu alan sayı/rakam içeremez.")
    if not re.match(r"^[a-zA-ZçğışöüÇĞİŞÖÜ\s.\-']+$", value):
        raise ValidationError("Bu alan sadece harf ve geçerli karakterler (. - ') içerebilir.")


class Yonetmen(models.Model):
    isim = models.CharField(max_length=100, validators=[validate_letters_only])
    biyografi = models.TextField(blank=True, null=True)
    fotograf = models.ImageField(upload_to="yonetmenler/", blank=True, null=True)

    def __str__(self):
        return self.isim


class Film(models.Model):
    baslik = models.CharField(max_length=200, validators=[validate_no_digits])
    yonetmen = models.ForeignKey(Yonetmen, on_delete=models.CASCADE, related_name="filmler")
    tur = models.CharField(max_length=50, validators=[validate_letters_only])
    puan = models.FloatField(
        validators=[
            MinValueValidator(0.0, message="Puan en az 0 olabilir."),
            MaxValueValidator(5.0, message="Puan en fazla 5 olabilir.")
        ]
    )
    imdb_puani = models.FloatField(
        validators=[
            MinValueValidator(0.0, message="IMDb Puanı en az 0.0 olabilir."),
            MaxValueValidator(10.0, message="IMDb Puanı en fazla 10.0 olabilir.")
        ],
        blank=True,
        null=True
    )
    yayin_yili = models.IntegerField(blank=True, null=True)
    sure = models.CharField(max_length=50, blank=True, null=True)
    fragman_url = models.URLField(blank=True, null=True)
    afis = models.ImageField(upload_to="afisler/", blank=True, null=True)
    arkaplan_resmi = models.ImageField(upload_to="arkaplanlar/", blank=True, null=True)
    ozet = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.baslik

