from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modelos/', views.index_modelos, name='lista_modelos'),
    path('modelos/<int:modelo_id>/', views.show_modelo, name='detalle_modelo'),
    path('tipos/', views.index_tipos, name='lista_tipos'),
    path('tipos/<int:tipo_id>/', views.show_tipo, name='detalle_tipo'),
    path('impactos/', views.index_impactos, name='lista_impactos'),
    path('impactos/<int:impacto_id>/', views.show_impacto, name='detalle_impacto'),
]