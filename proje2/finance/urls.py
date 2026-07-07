from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('sil/<int:yazi_id>/', views.yazi_sil, name='yazi_sil'), # <int:yazi_id> olarak düzelttik
    path('duzenle/<int:yazi_id>/', views.yazi_duzenle, name='yazi_duzenle'), # <int:yazi_id> olarak düzelttik
]