from django.shortcuts import render
from django.views.generic import View
from .models import About, Funcionario
from categories.models import Categoria


class Index(View):

    def get(self, *args, **kwargs):
        personalizacoes = About.objects.filter(
            publicado_about=True).order_by('-id')[:1]
        funcionarios = Funcionario.objects.filter(
            publicado=True).order_by('-id')
        categorias = Categoria.objects.all()

        context = {
            'personalizacoes': personalizacoes,
            'funcionarios': funcionarios,
            'categorias': categorias,
        }

        return render(self.request, 'about/index.html', context)
