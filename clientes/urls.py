from django.urls import path
from .views import index, create_clientes, delete_clientes, detail_clientes, update_clientes

urlpatterns = [
    path('', index, name='list_clientes'),
    path('new/', create_clientes, name='create_clientes'),
    path('delete/<int:id>/', delete_clientes, name='delete_clientes'),
    path('detail/', detail_clientes, name='detail_clientes'),
    path('update/<int:id>/', update_clientes, name='update_clientes')
]