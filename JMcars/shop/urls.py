from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.index, name='shop'),
    path('carro/<int:pk>', views.CarroDetalhes.as_view(), name='carro_detalhes'),
]
