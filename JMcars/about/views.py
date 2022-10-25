from django.shortcuts import render
from .models import About
from .models import Funcionario


def index(request):
    valor = About.objects.filter(publicado_about=True).order_by('-id')[:1]
    funcionario = Funcionario.objects.filter(
        publicado=True).order_by('id')

    return render(request, 'about/index.html', {
        'valores': valor, 'funcionarios': funcionario,
    })
