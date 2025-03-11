from django.db import models

class Categoria(models.Model):
    clave_tipo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    clave = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


