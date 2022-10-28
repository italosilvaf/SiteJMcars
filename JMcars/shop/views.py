from multiprocessing import context
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Shop
from .models import Car
from categories.models import Categoria


class CarView(ListView):
    model = Car
    template_name = 'shop/index.html'
    paginate_by = 12
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valores'] = Shop.objects.filter(
            publicado_shop=True).order_by('-id')[:1]
        context['categorias'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(publicado=True).order_by('-id')
        return qs


class CarroDetalhes(UpdateView):
    template_name = 'shop/carro_detalhes.html'
    model = Car
    context_object_name = 'car'
    fields = "__all__"


class CarroCategoria(ListView):
    template_name = 'shop/carro_categoria.html'
    model = Categoria
    context_object_name = 'categorias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valores'] = Shop.objects.filter(
            publicado_shop=True).order_by('-id')[:1]

        categoria = self.kwargs.get('nome_categoria', None)
        context['cars'] = Car.objects.filter(publicado=True,
                                             categoria_carro__nome_categoria__iexact=categoria).order_by('-id')
        return context
