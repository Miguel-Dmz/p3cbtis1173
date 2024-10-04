from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("contactos/",views.contactos,name="contactos"),
    path("empleados/",views.empleados,name="empleados"),
    path("calzado/",views.calzado,name="calzado"),
    path("sucursales/",views.sucursales,name="sucursales"),
    path("proveedores/",views.proveedores,name="proveedores"),
    path("venta/",views.venta,name="venta"),
]