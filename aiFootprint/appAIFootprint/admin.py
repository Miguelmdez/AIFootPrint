from django.contrib import admin
from .models import TipoModelo, ImpactoAmbiental, ModeloIA

# Register your models here.
admin.site.register(TipoModelo)
admin.site.register(ImpactoAmbiental)
admin.site.register(ModeloIA)