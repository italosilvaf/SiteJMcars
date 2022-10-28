from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarView.as_view(), name='shop'),
    path('carro/<int:pk>', views.CarroDetalhes.as_view(), name='carro_detalhes'),
    path('busca/', views.CarroBusca.as_view(), name='carro_busca'),
    path('categoria/<str:nome_categoria>',
         views.CarroCategoria.as_view(), name='carro_categorias'),
]
