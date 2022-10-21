from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Shop
from .models import Car


def index(request):
    valor = Shop.objects.filter(publicado_shop=True).order_by('-id')[:1]
    car = Car.objects.filter(publicado=True).order_by('-id')

    return render(request, 'shop/index.html', {
        'valores': valor, 'cars': car
    })
