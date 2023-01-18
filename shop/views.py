from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Shop
from .models import Car
from categories.models import Categoria, Cor


class CarView(ListView):
    model = Car
    template_name = 'shop/index.html'
    paginate_by = 12
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personalizacoes'] = Shop.objects.filter(
            publicado_shop=True).order_by('-id').first()
        context['categorias'] = Categoria.objects.all()
        context['cores'] = Cor.objects.all()

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('nome_categoria', None)

        if not categoria:
            qs = qs.filter(publicado=True).order_by('-id')
            return qs

        qs = qs.filter(
            categoria_carro__nome_categoria__iexact=categoria, publicado=True).order_by('-id')
        return qs


class CarroDetalhes(DetailView):
    template_name = 'shop/carro_detalhes.html'
    model = Car
    context_object_name = 'car'


class CarroBusca(CarView):

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo or termo is None:
            return qs

        qs = qs.filter(
            Q(modelo__icontains=termo) |
            Q(marca__nome_marca__icontains=termo) |
            Q(ano__icontains=termo) |
            Q(cor__nome_cor__icontains=termo) |
            Q(quilometragem__icontains=termo) |
            Q(motorizacao__icontains=termo) |
            Q(cambio__nome_cambio__icontains=termo) |
            Q(categoria_carro__nome_categoria__icontains=termo)
        )

        return qs


class CarroFiltro(CarView):

    def get_queryset(self):
        qs = super().get_queryset()
        cores_selecionadas = self.request.GET.getlist('filtro')
        lista_de_cores = []
        filtro = Q()

        for cor_selecionada in cores_selecionadas:
            if cor_selecionada is not None:
                lista_de_cores.append(cor_selecionada)

        for cor in lista_de_cores:
            filtro |= Q(cor__nome_cor__icontains=cor)

        print(filtro)

        qs = qs.filter(filtro)

        return qs
