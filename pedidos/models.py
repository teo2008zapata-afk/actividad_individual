from django.db import models

class pedido(models.Model):
    numero_pedido = models.CharField(max_length=100)
    nombre_cliente = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    total = models.PositiveIntegerField()
    estado = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_cliente