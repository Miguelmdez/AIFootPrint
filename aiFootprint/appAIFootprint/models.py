
from django.db import models


# Tipos de modelos de inteligencia artificial
class TipoModelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# Tipos de impacto ambiental
class ImpactoAmbiental(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# Modelos de inteligencia artificial
class ModeloIA(models.Model):
    nombre = models.CharField(max_length=100)
    desarrollador = models.CharField(max_length=100)
    descripcion = models.TextField()

    # Cada modelo pertenece a un tipo
    tipo = models.ForeignKey(
        TipoModelo,
        on_delete=models.CASCADE,
        related_name='modelos'
    )

    # Un modelo puede generar varios impactos
    # y un impacto puede estar asociado a varios modelos
    impactos = models.ManyToManyField(
        ImpactoAmbiental,
        related_name='modelos',
        blank=True
    )

    def __str__(self):
        return self.nombre
