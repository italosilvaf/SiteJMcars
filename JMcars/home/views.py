from django.shortcuts import render
from .models import Home


def index(request):
    valor = Home.objects.filter(publicado_home=True).order_by('-id')[:1]
    return render(request, 'home/index.html', {
        'valores': valor,
    })
