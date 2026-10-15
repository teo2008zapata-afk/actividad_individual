from django.db import models

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.positive.
    stock= models.positive.intergerfield
    fecha =
    
    def __str__(self):
        return self.nombres