from django.shortcuts import render, redirect, get_object_or_404

from .forms import FilmForm, YonetmenForm
from .models import Film, Yonetmen


def populer_filmler(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("populer_filmler")
    else:
        form = FilmForm()
    filmler = Film.objects.all()
    
    # Manşet film seçimi (Önce arkaplan resmi olanlardan en yüksek puanlıyı, yoksa genel en yüksek puanlıyı seç)
    manset_film = Film.objects.exclude(arkaplan_resmi="").order_by('-imdb_puani', '-puan').first()
    if not manset_film:
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
