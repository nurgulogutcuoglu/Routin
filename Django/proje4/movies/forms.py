from django import forms

from .models import Film, Yonetmen, Oyuncu


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


class OyuncuForm(forms.ModelForm):
    class Meta:
        model = Oyuncu
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
        fields = [
            "baslik", "yonetmen", "oyuncular", "tur", "puan", "imdb_puani",
            "yayin_yili", "sure", "fragman_url", "afis", "ozet"
        ]
        widgets = {
            'oyuncular': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = 'Bu alanın doldurulması zorunludur.'
                field.widget.attrs['placeholder'] = 'Zorunlu'
            else:
                field.widget.attrs['placeholder'] = 'İsteğe Bağlı'

        if 'yonetmen' in self.fields:
            self.fields['yonetmen'].empty_label = 'Yönetmen Seçin (Zorunlu)'

            # Oyuncular alanı için açıklama ekledik
        if 'oyuncular' in self.fields:
            self.fields['oyuncular'].help_text = 'Ctrl veya Cmd tuşuna basarak birden fazla oyuncu seçebilirsiniz.'

        # (puan, imdb_puani vb. diğer ayarlar olduğu gibi kalacak...)

        if 'puan' in self.fields:
            self.fields['puan'].widget.attrs.update({
                'min': '0',
                'max': '5',
                'step': '0.1',
                'placeholder': 'Puan (0-5)'
            })
            self.fields['puan'].error_messages.update({
                'invalid': 'Lütfen geçerli bir sayısal puan girin.',
            })

        if 'imdb_puani' in self.fields:
            self.fields['imdb_puani'].widget.attrs.update({
                'min': '0.0',
                'max': '10.0',
                'step': '0.1',
                'placeholder': 'IMDb Puanı (0-10)'
            })

        if 'yayin_yili' in self.fields:
            self.fields['yayin_yili'].widget.attrs.update({
                'placeholder': 'Örn: 2024'
            })

        if 'sure' in self.fields:
            self.fields['sure'].widget.attrs.update({
                'placeholder': 'Örn: 2s 15dk'
            })

        if 'fragman_url' in self.fields:
            self.fields['fragman_url'].widget.attrs.update({
                'placeholder': 'YouTube Fragman URL'
            })
