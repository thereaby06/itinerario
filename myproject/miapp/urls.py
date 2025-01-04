from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/editar/<int:pk>/', views.editar_servicio, name='editar_servicio'),
    path('servicios/eliminar/<int:pk>/', views.eliminar_servicio, name='eliminar_servicio'),
]

