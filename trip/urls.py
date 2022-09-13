from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('camping/', views.camping),
    path('corupa/', views.corupa),
    path('cozinha/', views.cozinha),
    path('mochila/', views.mochila),
    path('pico/', views.pico),
]
