from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servicos, name='lista_servicos'),
    path('buscar/', views.buscar_servicos, name='buscar_servicos'),
]
