from django import forms
from .models import Yazı

class YazıForm(forms.ModelForm):
    class Meta:
        model = Yazı
        fields = ['baslik', 'icerik', 'kategori', 'gorsel']