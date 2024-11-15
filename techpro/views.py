from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from .models import Techpro
from .forms import formTechpro
def Listar(request):
    techpro = Techpro.objects.all()
    return render(request, 'ListarSolicitud.html', {'techpro': techpro})

def Visualizar(request, pk):
    techpro = get_object_or_404(Techpro, pk=pk)
    return render(request, 'Visualizar.html', {'techpro': techpro})
def Crear(request):
    if request.method == 'POST':
        form = formTechpro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Listar')
    else:
        form = formTechpro()
    return render(request, 'Crear.html', {'form': form})
def Editar(request, pk):
    techpro = get_object_or_404(Techpro, pk=pk)
    if request.method == 'POST':
        form = formTechpro(request.POST, instance=techpro)
        if form.is_valid():
            form.save()
            return redirect('Listar')
    else:
        form = formTechpro(instance=techpro)
    return render(request, 'Crear.html', {'form': form})
def Eliminar(request, pk):
    techpro = get_object_or_404(Techpro, pk=pk)
    if request.method == 'POST':
        techpro.delete()
        return redirect('Listar')
    return render(request, 'EliminarSolicitud.html', {'techpro': techpro})