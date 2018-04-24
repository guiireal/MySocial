from django.urls import path
from perfis import views

urlpatterns = [
    path('perfil/<int:perfil_id>/', views.exibir, name='exibir'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('', views.index, name='index'),
]
