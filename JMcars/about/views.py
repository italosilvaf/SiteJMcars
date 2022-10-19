from django.shortcuts import render
from .models import About


def index(request):
    valor = About.objects.filter(publicado_pagina=True).order_by('-id')[:1]
    return render(request, 'about/index.html', {
        'valores': valor,
    })
