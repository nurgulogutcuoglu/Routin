from django.shortcuts import render, redirect, get_object_or_404
from .models import Yazı
from .forms import YazıForm


def anasayfa(request):
    if request.method == 'POST':
        form = YazıForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('anasayfa')
    else:
        form = YazıForm()

    # YENİLİK: Baştaki eksiyi (-) kaldırdık! Böylece yazılar eskiden yeniye sıralanacak,
    # yani yeni eklenen kart her zaman şeffaf + butonunun hemen soluna (sağ tarafa) eklenecek.
    yazilar = Yazı.objects.all().order_by('tarih')
    return render(request, 'finance/anasayfa.html', {'yazilar': yazilar, 'form': form})


# YENİLİK: Silme fonksiyonu
def yazi_sil(request, yazi_id):
    yazi = get_object_or_404(Yazı, id=yazi_id)
    yazi.delete()  # Veritabanından tık diye siler
    return redirect('anasayfa')


# YENİLİK: Düzenleme fonksiyonu
def yazi_duzenle(request, yazi_id):
    yazi = get_object_or_404(Yazı, id=yazi_id)
    if request.method == 'POST':
        form = YazıForm(request.POST, request.FILES, instance=yazi)  # Mevcut yazının üzerine yazar
        if form.is_valid():
            form.save()
            return redirect('anasayfa')
    else:
        form = YazıForm(instance=yazi)  # Formun içini mevcut yazı bilgileriyle doldurur

    yazilar = Yazı.objects.all().order_by('tarih')
    return render(request, 'finance/anasayfa.html', {'yazilar': yazilar, 'form': form, 'duzenlenecek_yazi': yazi})