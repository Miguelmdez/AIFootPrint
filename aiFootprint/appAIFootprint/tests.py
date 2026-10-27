from django.test import TestCase

from django.urls import reverse

from .models import ImpactoAmbiental, ModeloIA, TipoModelo


class ModeloViewsTests(TestCase):
    def setUp(self):
        self.tipo = TipoModelo.objects.create(
            nombre='Generación de texto',
            descripcion='Modelos que generan texto.',
        )
        self.impacto = ImpactoAmbiental.objects.create(
            nombre='Consumo energético',
            descripcion='Energía utilizada durante el entrenamiento y uso.',
        )
        self.modelo = ModeloIA.objects.create(
            nombre='Modelo de prueba',
            desarrollador='Desarrollador de prueba',
            descripcion='Descripción del modelo.',
            tipo=self.tipo,
        )
        self.modelo.impactos.add(self.impacto)

    def test_lista_modelos_muestra_modelos_y_tipo(self):
        response = self.client.get(reverse('lista_modelos'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index_modelos.html')
        self.assertContains(response, self.modelo.nombre)
        self.assertContains(response, self.tipo.nombre)
        self.assertContains(
            response,
            reverse('detalle_modelo', args=[self.modelo.pk]),
        )

    def test_lista_modelos_vacia_se_muestra_sin_error(self):
        ModeloIA.objects.all().delete()

        response = self.client.get(reverse('lista_modelos'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Todavía no hay modelos registrados.')

    def test_detalle_modelo_muestra_tipo_e_impactos(self):
        response = self.client.get(
            reverse('detalle_modelo', args=[self.modelo.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_modelo.html')
        self.assertContains(response, self.tipo.nombre)
        self.assertContains(response, self.impacto.nombre)


class TipoModeloViewsTests(TestCase):
    def setUp(self):
        self.tipo = TipoModelo.objects.create(
            nombre='Generación de texto',
            descripcion='Modelos que generan texto.',
        )
        self.modelo = ModeloIA.objects.create(
            nombre='Modelo de prueba',
            desarrollador='Desarrollador de prueba',
            descripcion='Descripción del modelo.',
            tipo=self.tipo,
        )

    def test_lista_tipos_muestra_tipo_y_enlace_al_detalle(self):
        response = self.client.get(reverse('lista_tipos'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index_tipos.html')
        self.assertContains(response, self.tipo.nombre)
        self.assertContains(
            response,
            reverse('detalle_tipo', args=[self.tipo.pk]),
        )

    def test_lista_tipos_vacia_se_muestra_sin_error(self):
        TipoModelo.objects.all().delete()

        response = self.client.get(reverse('lista_tipos'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'Todavía no hay tipos de modelo registrados.',
        )

    def test_detalle_tipo_muestra_modelos_asociados(self):
        response = self.client.get(
            reverse('detalle_tipo', args=[self.tipo.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_tipo.html')
        self.assertContains(response, self.modelo.nombre)
        self.assertContains(
            response,
            reverse('detalle_modelo', args=[self.modelo.pk]),
        )
