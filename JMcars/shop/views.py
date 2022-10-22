from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Shop
from .models import Car


def index(request):
    valor = Shop.objects.filter(publicado_shop=True).order_by('-id')[:1]
    car = Car.objects.filter(publicado=True).order_by('-id')

    contact_list = car
    paginator = Paginator(contact_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/index.html', {
        'valores': valor, 'cars': page_obj, 'page_obj': page_obj,
    })
