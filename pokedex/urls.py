from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.pokemon_list, name='pokemon_list'),
    path('detalle/<str:name>/', views.pokemon_detail, name='pokemon_detail'),
    path('nuevo/', views.pokemon_create, name='pokemon_create'),
    path('editar/<int:pk>/', views.pokemon_update, name='pokemon_update'),
    path('eliminar/<int:pk>/', views.pokemon_delete, name='pokemon_delete'),
]
