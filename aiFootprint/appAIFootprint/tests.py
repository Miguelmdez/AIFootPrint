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
