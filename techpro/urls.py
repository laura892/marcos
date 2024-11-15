from . import views
from django.urls import path

urlpatterns = [
    path('', views.Listar, name='Listar'),
    path('add/', views.Crear, name='Crear'),
    path('update/<int:pk>/', views.Editar, name='Editar'),
    path('delete/<int:pk>/', views.Eliminar, name='Eliminar'),
    path('detail/<int:pk>/', views.Visualizar, name='Visualizar'),
]