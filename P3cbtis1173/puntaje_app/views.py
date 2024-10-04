from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"index.html")

def contactos(request):
    return render(request,"contactos.html")

def empleados(request):
    return render(request,"empleados.html")

def calzado(request):
    return render(request,"calzado.html")

def sucursales(request):
    return render(request,"sucursales.html")

def proveedores(request):
    return render(request,"proveedores.html")

def venta(request):
    return render(request,"venta.html")