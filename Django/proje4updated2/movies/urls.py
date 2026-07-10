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

    # 1. Oyuncuların tamamının listelendiği sayfa adresi (/yonetmenler/ gibi)
    path("oyuncular/", views.oyuncular, name="oyuncular"),

    # 2. Tıklanan oyuncunun detay/biyografi sayfa adresi (/yonetmen/<id>/ gibi)
    # <int:oyuncu_id> kısmı, tıklanan oyuncunun benzersiz numarasını dinamik olarak adrese ekler
    path("oyuncu/<int:oyuncu_id>/", views.oyuncu_detay, name="oyuncu_detay"),

    # 3. Oyuncu düzenleme adresi
    path("oyuncu/duzenle/<int:oyuncu_id>/", views.oyuncu_duzenle, name="oyuncu_duzenle"),

    # 4. Oyuncu silme adresi
    path("oyuncu/sil/<int:oyuncu_id>/", views.oyuncu_sil, name="oyuncu_sil"),

    # --- API ADRESLERİ (ENDPOINT'LER) ---

    # Filmler API
    path("api/filmler/", views.FilmListAPIView.as_view(), name="api_film_listesi"),
    path("api/filmler/<int:pk>/", views.FilmDetailAPIView.as_view(), name="api_film_detayi"),

    # Yönetmenler API
    path("api/yonetmenler/", views.YonetmenListAPIView.as_view(), name="api_yonetmen_listesi"),
    path("api/yonetmenler/<int:pk>/", views.YonetmenDetailAPIView.as_view(), name="api_yonetmen_detayi"),

    # Oyuncular API
    path("api/oyuncular/", views.OyuncuListAPIView.as_view(), name="api_oyuncu_listesi"),
    path("api/oyuncular/<int:pk>/", views.OyuncuDetailAPIView.as_view(), name="api_oyuncu_detayi"),

]
