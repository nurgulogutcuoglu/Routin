from django import forms

from .models import Film, Yonetmen


class YonetmenForm(forms.ModelForm):
    class Meta:
        model = Yonetmen
        fields = ["isim", "biyografi", "fotograf"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = 'Bu alanın doldurulması zorunludur.'
                field.widget.attrs['placeholder'] = 'Zorunlu'


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ["baslik", "yonetmen", "tur", "puan", "afis", "ozet"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = 'Bu alanın doldurulması zorunludur.'
                field.widget.attrs['placeholder'] = 'Zorunlu'
        
        if 'yonetmen' in self.fields:
            self.fields['yonetmen'].empty_label = 'Yönetmen Seçin (Zorunlu)'
            
        if 'puan' in self.fields:
            self.fields['puan'].widget.attrs.update({
                'min': '0',
                'max': '5',
                'step': '0.1',
                'placeholder': 'Zorunlu'
            })
            self.fields['puan'].error_messages.update({
                'invalid': 'Lütfen geçerli bir sayısal puan girin.',
            })
