from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Carrito(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(default=0.0,max_digits=10, decimal_places=2)  
    precio_descuento = models.DecimalField(default=0.0,max_digits=10, decimal_places=2)

class Todos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(default=0.0,max_digits=10, decimal_places=2)  
    precio_descuento = models.DecimalField(default=0.0,max_digits=10, decimal_places=2)

class descuentos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
class populares(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"