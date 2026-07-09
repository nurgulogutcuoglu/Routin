from django.urls import path

from . import views

urlpatterns = [
    path("", views.populer_filmler, name="populer_filmler"),
    path("yonetmenler/", views.yonetmenler, name="yonetmenler"),
    path("film/<int:film_id>/", views.film_detay, name="film_detay"),
    path("yonetmen/<int:yonetmen_id>/", views.yonetmen_detay, name="yonetmen_detay"),

    # Düzenleme ve Silme Rotaları
    path("film/duzenle/<int:film_id>/", views.film_duzenle, name="film_duzenle"),
    path("film/sil/<int:film_id>/", views.film_sil, name="film_sil"),
    path("yonetmen/duzenle/<int:yonetmen_id>/", views.yonetmen_duzenle, name="yonetmen_duzenle"),
    path("yonetmen/sil/<int:yonetmen_id>/", views.yonetmen_sil, name="yonetmen_sil"),
]
