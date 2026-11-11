from django import forms
from .models import TipoModelo, ImpactoAmbiental, ModeloIA
#Andoni

# Formulario para los tipos de modelos de IA
class TipoModeloForm(forms.ModelForm):
    class Meta:
        model = TipoModelo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del tipo de modelo'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripcion del tipo de modelo',
                'rows': 3
            }),
        }


# Formulario para los impactos ambientales
class ImpactoAmbientalForm(forms.ModelForm):
    class Meta:
        model = ImpactoAmbiental
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del impacto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripcion del impacto ambiental',
                'rows': 3
            }),
        }


# Formulario para los modelos de inteligencia artificial
class ModeloIAForm(forms.ModelForm):
    class Meta:
        model = ModeloIA
        fields = ['nombre', 'desarrollador', 'descripcion', 'tipo', 'impactos']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del modelo de IA'
            }),
            'desarrollador': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del desarrollador'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripcion del modelo de IA',
                'rows': 4
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'impactos': forms.CheckboxSelectMultiple(),
        }