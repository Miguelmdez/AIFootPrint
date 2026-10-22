from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render

from .models import ModeloIA, TipoModelo, ImpactoAmbiental


# Devuelve el listado de modelos de IA
def index_modelos(request):
    modelos = get_list_or_404(
        ModeloIA.objects.order_by('nombre')
    )

    context = {'lista_modelos': modelos}

    return render(request, 'index_modelos.html', context)


# Devuelve los datos de un modelo concreto
def show_modelo(request, modelo_id):
    modelo = get_object_or_404(
        ModeloIA,
        pk=modelo_id
    )

    impactos = modelo.impactos.all()

    context = {
        'modelo': modelo,
        'impactos': impactos
    }

    return render(request, 'detail_modelo.html', context)


# Devuelve el listado de tipos de modelo
def index_tipos(request):
    tipos = get_list_or_404(
        TipoModelo.objects.order_by('nombre')
    )

    context = {'lista_tipos': tipos}

    return render(request, 'index_tipos.html', context)


# Devuelve los datos de un tipo de modelo
def show_tipo(request, tipo_id):
    tipo = get_object_or_404(
        TipoModelo,
        pk=tipo_id
    )

    modelos = tipo.modelos.all()

    context = {
        'tipo': tipo,
        'modelos': modelos
    }

    return render(request, 'detail_tipo.html', context)


# Devuelve el listado de impactos ambientales
def index_impactos(request):
    impactos = get_list_or_404(
        ImpactoAmbiental.objects.order_by('nombre')
    )

    context = {'lista_impactos': impactos}

    return render(request, 'index_impactos.html', context)


# Devuelve los datos de un impacto ambiental
def show_impacto(request, impacto_id):
    impacto = get_object_or_404(
        ImpactoAmbiental,
        pk=impacto_id
    )

    modelos = impacto.modelos.all()

    context = {
        'impacto': impacto,
        'modelos': modelos
    }

    return render(request, 'detail_impacto.html', context)


# Devuelve la portada de AI Footprint
def index(request):
    modelos = ModeloIA.objects.order_by('nombre')
    impactos = ImpactoAmbiental.objects.order_by('nombre')

# Muestra como mucho 6 elementos de cada
    context = {
        'modelos_destacados': modelos[:6], 
        'impactos': impactos[:6],
    }

    return render(request, 'index.html', context)