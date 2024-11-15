from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from .models import Empleados
from .forms import formEmpleados
def ListarEmpleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'Listar.html', {'empleados': empleados})

def BuscarEmpleado(request, pk):
    empleados = get_object_or_404(Empleados, pk=pk)
    return render(request, 'Buscar.html', {'empleado': empleados})
def CrearEmpleado(request):
    if request.method == 'POST':
        form = formEmpleados(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListarEmpleados')
    else:
        form = formEmpleados()
    return render(request, 'Agregar.html', {'form': form})
def ActualizarEmpleado(request, pk):
    empleados = get_object_or_404(Empleados, pk=pk)
    if request.method == 'POST':
        form = formEmpleados(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            return redirect('ListarEmpleados')
    else:
        form = formEmpleados(instance=empleados)
    return render(request, 'Agregar.html', {'form': form})
def EliminarEmpleado(request, pk):
    empleados = get_object_or_404(Empleados, pk=pk)
    if request.method == 'POST':
        empleados.delete()
        return redirect('ListarEmpleados')
    return render(request, 'Eliminar.html', {'empleados': empleados})