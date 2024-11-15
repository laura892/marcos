from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListarEmpleados, name='ListarEmpleados'),
    path('add/', views.CrearEmpleado, name='CrearEmpleado'),
    path('update/<int:pk>/', views.ActualizarEmpleado, name='ActualizarEmpleado'),
    path('delete/<int:pk>/', views.EliminarEmpleado, name='EliminarEmpleado'),
    path('detail/<int:pk>/', views.BuscarEmpleado, name='BuscarEmpleado'),
]