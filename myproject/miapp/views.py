from django.shortcuts import render, get_object_or_404, redirect 
from .models import Servicio 
from .forms import ServicioForm
# Create your views here.
def inicio(request):
    return render(request, 'miapp/inicio.html')

def servicios(request):
    return render(request, 'miapp/servicios.html')

def contacto(request):
    return render(request, 'miapp/contacto.html')

def lista_servicios(request):
    query = request.GET.get('q')
    if query:
        servicios = Servicio.objects.filter(moto_cliente__icontains=query)
    else:
        servicios = Servicio.objects.all()
    return render(request, 'miapp/lista_servicios.html', {'servicios': servicios, 'query': query})


def agregar_servicio(request): 
    if request.method == 'POST': 
        form = ServicioForm(request.POST) 
        if form.is_valid(): form.save() 
        return redirect('lista_servicios')
    else: 
        form = ServicioForm() 
    return render(request, 'miapp/agregar_servicio.html', {'form': form})

def editar_servicio(request, pk): 
    servicio = get_object_or_404(Servicio, pk=pk) 
    if request.method == 'POST': 
        form = ServicioForm(request.POST, instance=servicio) 
        if form.is_valid(): form.save() 
        return redirect('lista_servicios')
    else: 
        form = ServicioForm(instance=servicio)
    return render(request, 'miapp/editar_servicio.html', {'form': form})

def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('lista_servicios')
    return render(request, 'miapp/eliminar_servicio.html', {'servicio': servicio})
