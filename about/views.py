from django.shortcuts import render
from django.views.generic import View
from .models import About, Funcionario
from categories.models import EstadoDeConservacao, Categoria


class Index(View):

    def get(self, *args, **kwargs):
        personalizacoes = About.objects.filter(
            publicado_about=True).order_by('-id').first()
        funcionarios = Funcionario.objects.filter(
            publicado=True).order_by('-id')
        estados_de_conservacao = EstadoDeConservacao.objects.all()
        categorias = Categoria.objects.all()

        context = {
            'personalizacoes': personalizacoes,
            'funcionarios': funcionarios,
            'estados_de_conservacao': estados_de_conservacao,
            'categorias': categorias,
        }

        return render(self.request, 'about/index.html', context)
