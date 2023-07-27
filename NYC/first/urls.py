from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='home' ),
    path('about', views.about, name ='about'),
    path('contacts', views.contacts, name ='contacts'),
    path('Wardrope', views.Wardrope, name ='Wardrope'),
    path('cars_base/', views.cars_base, name ='cars_base'),
    path('cars_base/<myid>', views.cars_base, name ='cars_base'),
    path('music_base/', views.music_base, name ='music_base'),
    path('music_base/<myid>', views.music_base, name ='music_base'),
    
]
