from django.shortcuts import render, redirect, get_object_or_404

# Form import:
from .forms import FilmForm, YonetmenForm, OyuncuForm
# Model import:
from .models import Film, Yonetmen, Oyuncu


def populer_filmler(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("populer_filmler")
    else:
        form = FilmForm()
    filmler = Film.objects.all()

    # Manşet film seçimi (En yüksek puanlı film manşet olur)
    manset_film = Film.objects.order_by('-imdb_puani', '-puan').first()

    # Filmleri türlerine göre gruplama
    genres_dict = {}
    for film in filmler:
        if film.tur not in genres_dict:
            genres_dict[film.tur] = []
        genres_dict[film.tur].append(film)

    return render(request, "movies/filmler.html", {
        "filmler": filmler,
        "form": form,
        "manset_film": manset_film,
        "genres_dict": genres_dict,
    })


def yonetmenler(request):
    if request.method == "POST":
        form = YonetmenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("yonetmenler")
    else:
        form = YonetmenForm()
    tum_yonetmenler = Yonetmen.objects.all()
    return render(request, "movies/yonetmenler.html", {"yonetmenler": tum_yonetmenler, "form": form})


def film_detay(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    return render(request, "movies/detay.html", {"film": film})


def yonetmen_detay(request, yonetmen_id):
    yonetmen = get_object_or_404(Yonetmen, id=yonetmen_id)
    filmler = yonetmen.filmler.all()
    return render(request, "movies/yonetmen_detay.html", {"yonetmen": yonetmen, "filmler": filmler})


def film_duzenle(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect("populer_filmler")
    else:
        form = FilmForm(instance=film)
    return render(request, "movies/duzenle_form.html", {"form": form, "baslik": "Filmi Düzenle"})


def film_sil(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    film.delete()
    return redirect("populer_filmler")


def yonetmen_duzenle(request, yonetmen_id):
    yonetmen = get_object_or_404(Yonetmen, id=yonetmen_id)
    if request.method == "POST":
        form = YonetmenForm(request.POST, request.FILES, instance=yonetmen)
        if form.is_valid():
            form.save()
            return redirect("yonetmenler")
    else:
        form = YonetmenForm(instance=yonetmen)
    return render(request, "movies/duzenle_form.html", {"form": form, "baslik": "Yönetmeni Düzenle"})


def yonetmen_sil(request, yonetmen_id):
    yonetmen = get_object_or_404(Yonetmen, id=yonetmen_id)
    yonetmen.delete()
    return redirect("yonetmenler")


def oyuncular(request):
    # Eğer tarayıcıdan POST isteği geldiyse (Kullanıcı formu doldurup "Kaydet"e bastıysa)
    if request.method == "POST":
        # Kullanıcının girdiği metinleri (request.POST) ve yüklediği resmi (request.FILES) forma yükle
        form = OyuncuForm(request.POST, request.FILES)

        # Formdaki veriler (isim doğrulama, boş alanlar vb.) kurallara uygun mu kontrol et
        if form.is_valid():
            form.save()  # Her şey doğruysa veritabanına kaydet (Yeni satır ekle)
            return redirect("oyuncular")  # Tarayıcıyı tekrar temiz bir liste sayfasına yönlendir

    # Eğer tarayıcıdan GET isteği geldiyse (Kullanıcı sayfayı ilk kez açıyorsa)
    else:
        form = OyuncuForm()  # Arayüzde gösterilmek üzere boş bir form nesnesi oluştur

    # Veritabanındaki OYUNCU tablosundaki tüm satırları çek
    tum_oyuncular = Oyuncu.objects.all()

    # HTML şablonuna (oyuncular.html) hem oyuncu listesini hem de formu gönder
    return render(request, "movies/oyuncular.html", {
        "oyuncular": tum_oyuncular,
        "form": form
    })


def oyuncu_detay(request, oyuncu_id):
    # URL'den gelen 'oyuncu_id'ye sahip oyuncuyu veritabanında ara.
    # Eğer öyle bir oyuncu yoksa kullanıcıya "404 Sayfa Bulunamadı" hatası döndür.
    oyuncu = get_object_or_404(Oyuncu, id=oyuncu_id)

    # Django'nun ManyToMany (Çoka Çok) ilişkisi sayesinde;
    # Bu oyuncunun ilişkili olduğu tüm filmleri tek satırda çekiyoruz.
    # 'related_name="filmler"' demiştik, bu sayede 'oyuncu.filmler.all()' bize listeyi verir.
    filmler = oyuncu.filmler.all()

    # HTML şablonuna (oyuncu_detay.html) bu oyuncuyu ve oynadığı filmleri gönder
    return render(request, "movies/oyuncu_detay.html", {
        "oyuncu": oyuncu,
        "filmler": filmler
    })


def oyuncu_duzenle(request, oyuncu_id):
    # Güncellenecek oyuncuyu bul
    oyuncu = get_object_or_404(Oyuncu, id=oyuncu_id)

    # Form gönderildiyse (Güncellemeleri Kaydet)
    if request.method == "POST":
        # Formu doldur ama bu sefer yeni kayıt açmak yerine mevcut 'oyuncu'yu güncelle (instance=oyuncu)
        form = OyuncuForm(request.POST, request.FILES, instance=oyuncu)
        if form.is_valid():
            form.save()  # Değişiklikleri veritabanında güncelle (SQL UPDATE)
            return redirect("oyuncular")

    # Düzenleme sayfası ilk açıldığında (GET)
    else:
        # Formu, mevcut oyuncunun bilgileriyle dolu olarak arayüze gönder
        form = OyuncuForm(instance=oyuncu)

    # Yönetmen düzenlemede kullandığımız ortak tasarım formunu (duzenle_form.html) kullanıyoruz
    return render(request, "movies/duzenle_form.html", {
        "form": form,
        "baslik": "Oyuncuyu Düzenle"
    })


def oyuncu_sil(request, oyuncu_id):
    # Silinecek oyuncuyu bul
    oyuncu = get_object_or_404(Oyuncu, id=oyuncu_id)

    # Veritabanından bu satırı sil (SQL DELETE)
    oyuncu.delete()

    # Silme işleminden sonra kullanıcıyı tekrar oyuncular listesine gönder
    return redirect("oyuncular")
