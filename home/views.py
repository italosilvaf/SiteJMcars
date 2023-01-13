from django.shortcuts import render
from categories.models import Categoria
from .models import Home, QualidadesHome
from django.views.generic import View
from shop.models import Car


class Index(View):

    def get(self, *args, **kwargs):
        personalizacoes = Home.objects.filter(
            publicado_home=True).order_by('-id').first()
        cars = Car.objects.filter(publicado=True).order_by('-id')[:5]
        categorias = Categoria.objects.all()
        qualidades = QualidadesHome.objects.filter(
            publicado_qualidade=True)

        context = {
            'personalizacoes': personalizacoes,
            'cars': cars,
            'categorias': categorias,
            'qualidades': qualidades,
        }

        return render(self.request, 'home/index.html', context)
