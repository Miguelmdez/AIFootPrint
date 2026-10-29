Prompt:
voy a hacer el siguiente proyecto de ingenieria web usando tecnologias html, django y css, me podrias dar alguna plantilla adecuada para la realizacion del proyecto:Propuesta de proyecto “AI Footprint”
El proyecto “AI Footprint” deberá implementar un sitio web en el que se muestre información sobre el coste ambiental de diferentes modelos y servicios de inteligencia artificial (ChatGPT, Gemini, Claude, Midjourney, Stable Diffusion, Sora, etc.), clasificados por su tipo (modelo de lenguaje, generación de imágenes, generación de vídeo, reconocimiento de voz, conducción autónoma, etc.) y por los tipos de impacto ambiental que generan (consumo eléctrico, consumo de agua para refrigeración, emisiones de CO₂, residuos electrónicos, extracción de minerales críticos, etc.), teniendo en cuenta que un mismo modelo puede generar varios tipos
de impacto.

También podrán ver los detalles de cada tipo de modelo y de cada tipo
de impacto, incluida la lista de modelos en cada caso.

[E2] Funcionalidades básicas

• Personalización de una plantilla (estructura de varios niveles) y sus estilos.

• Visualizar la portada de “AI Footprint”, mostrando un modelo de cada tipo (p.
ej. el que mayor consumo energético estimado tenga o el criterio que queráis).

• Visualizar la lista de modelos, que además permita ir a otra vista para ver los
detalles de un modelo concreto, incluido el nombre de su tipo y la lista de tipos
de impacto ambiental que genera.

• Visualizar la lista de tipos de modelo, que además permita ir a otra vista para
ver los detalles de un tipo de modelo, incluida la lista de modelos asociados.

• Visualizar la lista de tipos de impacto, que además permita ir a otra vista para
ver los detalles de un tipo de impacto, incluida la lista de modelos asociados.
…
¡Claro! Para tu proyecto de Ingeniería Web “AI Footprint”, te recomiendo crear una plantilla con Django Templates, HTML y CSS, utilizando una estructura de navegación común para todas las páginas. Así podrás cumplir los requisitos de la práctica sin complicar demasiado el desarrollo.

La idea es diseñar una web que funcione como un catálogo de modelos de inteligencia artificial y permita explorar sus posibles impactos ambientales mediante fichas, categorías y relaciones entre modelos e impactos.

1. Plantilla visual recomendada
Te propongo un diseño moderno, inspirado en una plataforma de divulgación tecnológica y sostenibilidad.



*Boceto conceptual de la portada: paleta verde oscuro, fondos claros, tarjetas y navegación sencilla. Puedes reproducirlo con HTML y CSS sin utilizar React ni JavaScript.

La plantilla tendría un menú principal con cinco apartados:

Inicio: presentación del proyecto y modelos destacados.

Modelos: catálogo de modelos de IA.

Tipos de modelo: lenguaje, imágenes, vídeo, voz, conducción autónoma, etc.

Impactos ambientales: energía, agua, CO₂, residuos electrónicos y minerales críticos.

Acerca del proyecto: objetivo, metodología y fuentes de información.

2. Estructura del proyecto Django
Para que el proyecto sea fácil de mantener y cumpla los requisitos de la asignatura, te recomiendo separar la aplicación en modelos, vistas, URLs y plantillas.

ai_footprint/
├── manage.py
├── ai_footprint/
│   ├── settings.py
│   └── urls.py
└── footprint/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── templates/
    │   └── footprint/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── modelos/
    │       │   ├── lista.html
    │       │   └── detalle.html
    │       ├── tipos_modelo/
    │       │   ├── lista.html
    │       │   └── detalle.html
    │       └── impactos/
    │           ├── lista.html
    │           └── detalle.html
    └── static/
        └── footprint/
            └── css/
                └── estilos.css
La clave es base.html: contendrá la cabecera, el menú, el contenido común y el pie de página. Las demás páginas heredarán esa plantilla con {% extends %}, evitando repetir código.

3. Diseña la base de datos
Como un modelo puede tener varios impactos y un impacto puede estar asociado a varios modelos, necesitas relaciones entre tablas.

ModeloIA

nombre · descripción · desarrollador

Muchos a muchos

Muchos a muchos

TipoModelo

Lenguaje, imagen, vídeo...

ImpactoAmbiental

Agua, energía, CO₂...

En Django, puedes representar este diseño mediante tres modelos y dos relaciones ManyToManyField.

footprint/models.py

from django.db import models


class TipoModelo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class ImpactoAmbiental(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class ModeloIA(models.Model):
    nombre = models.CharField(max_length=150)
    desarrollador = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.ForeignKey(
        TipoModelo,
        on_delete=models.PROTECT,
        related_name="modelos"

Esta estructura permite:

Un tipo de modelo, como «Generación de imágenes», asociado a muchos modelos.

Un modelo, como ChatGPT, asociado a varios impactos ambientales.

Un impacto, como el consumo eléctrico, relacionado con muchos modelos.

Importante: no todos los modelos publican datos ambientales comparables. El consumo energético debe documentarse con su fuente, unidad y alcance (por ejemplo, entrenamiento o inferencia); no conviene inventar cifras ni comparar estimaciones con metodologías distintas.

4. Plantilla principal: base.html
Esta es la plantilla que utilizarán todas las páginas. Incluye navegación, contenido dinámico y pie de página.


{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}AI Footprint{% endblock %}</title>
    <link rel="stylesheet"
          href="{% static 'footprint/css/estilos.css' %}">
</head>
<body>

    <header class="cabecera">
        <a href="{% url 'inicio' %}" class="logo">
            <span class="logo-icono">♧</span>
            AI Footprint
        </a>

        <nav class="navegacion">
            <a href="{% url 'inicio' %}">Inicio</a>
            <a href="{% url 'lista_modelos' %}">Modelos</a>
            <a href="{% url 'lista_tipos' %}">Tipos de modelo</a>
            <a href="{% url 'lista_impactos' %}">Impactos</a>
        </nav>
    </header>

    <main class="contenedor">
        {% block content %}
        {% endblock %}
    </main>

    <footer class="pie">
        <p>AI Footprint · Inteligencia artificial y sostenibilidad</p>
        <p>Proyecto académico de Ingeniería Web</p>
    </footer>

</body>
</html>

5. Hoja de estilos: estilos.css
Esta hoja de estilos proporciona la estética verde y minimalista del boceto anterior. Es CSS puro, sin necesidad de Bootstrap.


:root {
    --verde-oscuro: #173d30;
    --verde: #32734b;
    --verde-claro: #dcecdf;
    --fondo: #f5f7f3;
    --blanco: #ffffff;
    --texto: #25352d;
    --texto-secundario: #68786d;
    --borde: #dfe7df;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: var(--fondo);
    color: var(--texto);
    line-height: 1.6;
}

a {
    color: inherit;
    text-decoration: none;
}

.cabecera {
    background: var(--verde-oscuro);
    color: white;
    padding: 18px 7%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    flex-wrap: wrap;
}

.logo {
    font-size: 1.4rem;
    font-weight: bold;
}

.logo-icono {
    color: #b8e4b0;
    margin-right: 8px;
}

.navegacion {
    display: flex;
    gap: 22px;
    flex-wrap: wrap;
}

.navegacion a {
    color: #e0ece4;
    font-size: 0.95rem;
}

.navegacion a:hover {
    color: #b8e4b0;
}

.contenedor {
    width: min(1100px, 90%);
    margin: 40px auto;
    min-height: 65vh;
}

.hero {
    padding: 48px 36px;
    background: var(--verde-oscuro);
    color: white;
    border-radius: 18px;
    margin-bottom: 36px;
}

.hero h1 {
    font-size: clamp(2rem, 5vw, 3.2rem);
    line-height: 1.15;
    max-width: 720px;
}

.hero p {
    max-width: 650px;
    color: #d5e4da;
}

.boton {
    display: inline-block;
    padding: 11px 18px;
    background: #b8e4b0;
    color: #173d30;
    border-radius: 8px;
    font-weight: bold;
    margin-top: 10px;
}

.grid {
    display: grid;
    grid-template-columns:
        repeat(auto-fit, minmax(min(100%, 240px), 1fr));
    gap: 22px;
}

.tarjeta {
    background: var(--blanco);
    padding: 24px;
    border: 1px solid var(--borde);
    border-radius: 14px;
    transition: transform 0.2s, box-shadow 0.2s;
}

.tarjeta:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px #173d3012;
}

.tarjeta h3 {
    color: var(--verde-oscuro);
    margin-top: 0;
}

.etiqueta {
    display: inline-block;
    background: var(--verde-claro);
    color: var(--verde-oscuro);
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
}

.texto-secundario {
    color: var(--texto-secundario);
}

.pie {
    text-align: center;
    padding: 25px;
    background: #e9eee8;
    color: var(--texto-secundario);
    margin-top: 50px;
    font-size: 0.9rem;
}

@media (max-width: 600px) {
    .cabecera {
        padding: 18px 5%;
    }

    .navegacion {
        gap: 12px;
    }

    .contenedor {
        margin: 24px auto;
    }

    .hero {
        padding: 28px 22px;
    }
}























Prompt:
con el siguiente models.py, rellename la bdd con algunos datos de muestra:
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
quiero hacerlo como en el siguiente ejemplo: Añade y consulta registros desde la API de Django
Accede al intérprete interactivo de Django escribiendo el siguiente comando:
python manage.py shell
Una vez dentro, ya puedes comenzar a crear y consultar registros.
>>> from appEmpresaDjango.models import Departamento, Habilidad, Empleado  >>> departamento = Departamento(nombre="Oficina Tecnica", telefono="945010101")  >>> departamento.save()  # Django le asigna un id.  >>> departamento.id  1    # Acceder a sus atributos  >>> departamento.nombre  'Oficina Tecnica'    >>> Departamento.objects.all()  <QuerySet [<Departamento: Departamento object (1)>]>    >>> Departamento.objects.filter(nombre__contains='Oficina').count()  1    # Mostrar los empleados de un departamento.  >>> departamento.empleado_set.all()  <QuerySet []>    # Crear un empleado, indicando el departamento.  >>> empleado = Empleado(departamento=departamento, nombre="Markel Ugalde", fecha_nacimiento='1988-06-12', antiguedad="12")  >>> departamento.save()      # Opción alternativa para crear empleados a partir del departamento:  >>> departamento.empleado_set.create(nombre='Mikel Uriarte', fecha_nacimiento='1985-01-23')  <Empleado: Empleado object (1)>    >>>> departamento.empleado_set.create(nombre='Ane Labastida', fecha_nacimiento='1987-12-14')  <Empleado: Empleado object (2)>    empleado = departamento.empleado_set.create(nombre='Luken Abarra', fecha_nacimiento='1989-05-12')    # Es posible acceder desde el hijo a su padre.  >>> empleado.departamento  <Departamento: Departamento object (1)>    >>> empleado.departamento.nombre  'Oficina Tecnica'    # Podemos conseguir un empleado por su primary key:  empleado = Empleado.objects.get(pk=1)    # También es posible acceder desde el padre a todos sus hijos.  >>> departamento.empleado_set.all()  <QuerySet [<Empleado: Empleado object (1)>, <Empleado: Empleado object (2)>, <Empleado: Empleado object (3)>]>    >>>> departamento.empleado_set.count()  3    >>>> quit()

















Puedes rellenar la base de datos de AI Footprint directamente desde el intérprete interactivo de Django, igual que en tu ejemplo, sin crear ningún archivo adicional.
Primero, abre una terminal en la carpeta donde está manage.py y ejecuta:
python manage.py shell
Una vez dentro, sigue estos pasos.
1. Importar los modelos
>>> from appAIFootprint.models import TipoModelo, ImpactoAmbiental, ModeloIA
2. Crear tipos de modelos de IA
>>> tipo1 = TipoModelo(nombre="Modelos de lenguaje", descripcion="Modelos de inteligencia artificial capaces de comprender y generar texto.")>>> tipo1.save()>>> tipo2 = TipoModelo(nombre="Generación de imágenes", descripcion="Modelos que generan imágenes a partir de descripciones de texto.")>>> tipo2.save()>>> tipo3 = TipoModelo(nombre="Reconocimiento de voz", descripcion="Modelos que procesan audio y convierten la voz en texto.")>>> tipo3.save()>>> tipo4 = TipoModelo(nombre="Modelos multimodales", descripcion="Modelos que pueden procesar diferentes tipos de información, como texto, imágenes y audio.")>>> tipo4.save()
Puedes consultar los registros creados:
>>> TipoModelo.objects.all()>>> TipoModelo.objects.count()4
3. Crear impactos ambientales
>>> impacto1 = ImpactoAmbiental(nombre="Consumo energético", descripcion="Electricidad necesaria para entrenar y ejecutar modelos de inteligencia artificial.")>>> impacto1.save()>>> impacto2 = ImpactoAmbiental(nombre="Emisiones de CO2", descripcion="Emisiones de gases de efecto invernadero asociadas al consumo energético.")>>> impacto2.save()>>> impacto3 = ImpactoAmbiental(nombre="Consumo de agua", descripcion="Agua utilizada directa o indirectamente para refrigerar los centros de datos.")>>> impacto3.save()>>> impacto4 = ImpactoAmbiental(nombre="Uso de materias primas", descripcion="Recursos naturales necesarios para fabricar los componentes electrónicos.")>>> impacto4.save()>>> impacto5 = ImpactoAmbiental(nombre="Residuos electrónicos", descripcion="Residuos generados por equipos informáticos y componentes electrónicos al final de su vida útil.")>>> impacto5.save()
Comprueba que se han guardado:
>>> ImpactoAmbiental.objects.all()>>> ImpactoAmbiental.objects.count()5
4. Crear modelos de inteligencia artificial
Cada modelo necesita un tipo, porque el campo tipo de ModeloIA es una clave foránea (ForeignKey).
>>> modelo1 = ModeloIA(nombre="GPT-4o", desarrollador="OpenAI", descripcion="Modelo multimodal capaz de comprender y generar texto, procesar imágenes y trabajar con audio.", tipo=tipo1)>>> modelo1.save()>>> modelo2 = ModeloIA(nombre="Claude", desarrollador="Anthropic", descripcion="Familia de modelos de inteligencia artificial orientados a la comprensión y generación de texto.", tipo=tipo1)>>> modelo2.save()>>> modelo3 = ModeloIA(nombre="Llama", desarrollador="Meta", descripcion="Familia de modelos de lenguaje que puede utilizarse en diferentes aplicaciones.", tipo=tipo1)>>> modelo3.save()>>> modelo4 = ModeloIA(nombre="DALL-E", desarrollador="OpenAI", descripcion="Modelo de inteligencia artificial que genera imágenes a partir de instrucciones escritas.", tipo=tipo2)>>> modelo4.save()>>> modelo5 = ModeloIA(nombre="Stable Diffusion", desarrollador="Stability AI", descripcion="Modelo de generación de imágenes a partir de descripciones de texto.", tipo=tipo2)>>> modelo5.save()>>> modelo6 = ModeloIA(nombre="Whisper", desarrollador="OpenAI", descripcion="Modelo de reconocimiento automático de voz capaz de transcribir audio.", tipo=tipo3)>>> modelo6.save()>>> modelo7 = ModeloIA(nombre="Gemini", desarrollador="Google", descripcion="Familia de modelos multimodales que trabaja con distintos tipos de información.", tipo=tipo4)>>> modelo7.save()>>> modelo8 = ModeloIA(nombre="DeepSeek", desarrollador="DeepSeek", descripcion="Familia de modelos de inteligencia artificial orientados al razonamiento y la generación de texto.", tipo=tipo1)>>> modelo8.save()
Consulta los modelos:
>>> ModeloIA.objects.all()>>> ModeloIA.objects.count()8
5. Asociar modelos con impactos ambientales
Como impactos es un campo ManyToManyField, primero debes guardar el modelo y después asociarle los impactos.
Por ejemplo, para asociar GPT-4o con el consumo energético, las emisiones de CO2 y el consumo de agua:
>>> modelo1.impactos.add(impacto1, impacto2, impacto3)
Asocia también impactos a los demás modelos:
>>> modelo2.impactos.add(impacto1, impacto2, impacto3)>>> modelo3.impactos.add(impact1, impacto2, impacto4)>>> modelo4.impactos.add(impacto1, impacto2, impacto4, impacto5)>>> modelo5.impactos.add(impacto1, impacto2, impacto4, impacto5)>>> modelo6.impactos.add(impacto1, impacto2)>>> modelo7.impactos.add(impacto1, impacto2, impacto3)>>> modelo8.impactos.add(impacto1, impacto2, impacto4)
Estas asociaciones son datos de muestra para practicar, no mediciones científicas verificadas del impacto concreto de cada modelo.
6. Consultar las relaciones entre los modelos
Puedes consultar los impactos asociados a un modelo:
>>> modelo1.impactos.all()
Consultar cuántos impactos tiene:
>>> modelo1.impactos.count()3
Consultar el nombre de cada impacto:
>>> for impacto in modelo1.impactos.all():...     print(impacto.nombre)
También puedes consultar los modelos asociados a un impacto:
>>> impacto1.modelos.all()
Esto funciona porque definiste related_name='modelos' en el campo impactos de ModeloIA.
Para consultar todos los modelos de lenguaje:
>>> TipoModelo.objects.get(nombre="Modelos de lenguaje").modelos.all()
Y para buscar los modelos desarrollados por OpenAI:
>>> ModeloIA.objects.filter(desarrollador="OpenAI")
7. Comprobar todos los registros
Al terminar, ejecuta estas consultas:
>>> TipoModelo.objects.count()4>>> ImpactoAmbiental.objects.count()5>>> ModeloIA.objects.count()8
Si los resultados son 4, 5 y 8, respectivamente, los datos se han guardado correctamente.
Finalmente, sal del intérprete:
>>> quit()
Importante: ejecuta estos comandos una sola vez sobre una base de datos vacía. Si vuelves a ejecutarlos, Django intentará crear registros duplicados. Si necesitas repetir el proceso, podemos utilizar get_or_create() para evitar duplicados.



*NOTA: IMAGENES CREADAS POR IA GENERATIVA. USER: admin, PASSWORD: admin

REPO: https://github.com/Miguelmdez/AIFootPrint
