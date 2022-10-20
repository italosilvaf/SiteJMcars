from django.shortcuts import render
from .models import Shop


def index(request):
    valor = Shop.objects.filter(publicado_shop=True).order_by('-id')[:1]
    return render(request, 'shop/index.html', {
        'valores': valor,
    })
