from django.shortcuts import render, redirect
from .models import Clientes
def index(request):
    clientes = Clientes.objects.all()
    return render(request, 'index.html', {'clientes': clientes})

def create_clientes(request):
    clientes = Clientes(Nombre=request.POST['nombre'], Año=request.POST['año'], email=request.POST['email'],
                Contraseña=request.POST['contraseña'])
    clientes.save()
    return redirect('/clientes/')

def delete_clientes(request, id):
    clientes = Clientes.objects.get(id=id)
    clientes.delete()
    return redirect('/clientes/')
# Create your views here.

def detail_clientes(request):
    print(request.POST['id'])
    id=request.POST['id']
    clientes = Clientes.objects.all()
    try:
        cliente = Clientes.objects.get(id=id)
    except Clientes.DoesNotExist:
        return render(request, 'index.html', {'clientes': clientes})

    return render(request, 'index.html', {'clienteid': cliente,'clientes': clientes})


def update_clientes(request, id):
    # Consulta el usuario por ID
    cliente= Clientes.objects.get(id=id)

    if request.method == 'POST':
        # Actualiza los campos del usuario con los datos del formulario
        cliente.Nombre = request.POST.get('Nombre')
        cliente.Año = request.POST.get('Año')
        cliente.email = request.POST.get('email')

        # Valida y guarda la actualización
        cliente.save()

        # Redirige a la lista de usuarios después de la actualización
        return redirect('/clientes/')

    # Si es una solicitud GET, renderiza el formulario de actualización
    return redirect('/clientes/')

