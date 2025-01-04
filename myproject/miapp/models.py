from django.db import models

# Create your models here.

class Servicio(models.Model):
    fecha = models.DateField()
    moto_cliente = models.CharField(max_length=100)
    tipo_servicio = models.CharField(max_length=100, choices=[
        ('revision', 'Revisión'),
        ('mantenimiento_preventivo', 'Mantenimiento Preventivo'),
        ('mantenimiento_general', 'Mantenimiento General'),
        ('otro', 'Otro'),
    ])
    descripcion = models.TextField()
    cobro = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.moto_cliente} - {self.tipo_servicio}'
