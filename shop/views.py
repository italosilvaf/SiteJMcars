from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Shop
from .models import Car
from categories.models import EstadoDeConservacao, Categoria, Cor, Marca, Cambio


class CarView(ListView):
    model = Car
    template_name = 'shop/index.html'
    paginate_by = 12
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personalizacoes'] = Shop.objects.filter(
            publicado_shop=True).order_by('-id').first()
        context['estados_de_conservacao'] = EstadoDeConservacao.objects.all()
        context['categorias'] = Categoria.objects.all()
        context['marcas'] = Marca.objects.all()
        context['cores'] = Cor.objects.all()
        context['cambios'] = Cambio.objects.all()

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados_de_conservacao'] = EstadoDeConservacao.objects.all()
        context['categorias'] = Categoria.objects.all()

        return context


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
        filtro = []

        # Filtro Estado de Conservação
        estados_de_conservacao_selecionadas = self.request.GET.getlist(
            'filtro-estados_de_conservacao')
        lista_de_estados_de_conservacaos = []
        filtro_estados_de_conservacao = Q()

        for estado_de_conservacao_selecionadas in estados_de_conservacao_selecionadas:
            if estado_de_conservacao_selecionadas is not None:
                lista_de_estados_de_conservacaos.append(
                    estado_de_conservacao_selecionadas)

        for estado_de_conservacao in lista_de_estados_de_conservacaos:
            filtro_estados_de_conservacao |= Q(
                categoria_carro__nome_categoria=estado_de_conservacao)

        # Filtro Marcas
        marcas_selecionadas = self.request.GET.getlist('filtro-marcas')
        lista_de_marcas = []
        filtro_marcas = Q()

        for marca_selecionadas in marcas_selecionadas:
            if marca_selecionadas is not None:
                lista_de_marcas.append(marca_selecionadas)

        for marca in lista_de_marcas:
            filtro_marcas |= Q(marca__nome_marca=marca)

        # Filtro Cores
        cores_selecionadas = self.request.GET.getlist('filtro-cores')
        lista_de_cores = []
        filtro_cores = Q()

        for cor_selecionada in cores_selecionadas:
            if cor_selecionada is not None:
                lista_de_cores.append(cor_selecionada)

        for cor in lista_de_cores:
            filtro_cores |= Q(cor__nome_cor=cor)

        # Filtro Câmbios
        cambios_selecionados = self.request.GET.getlist('filtro-cambios')
        lista_de_cambios = []
        filtro_cambios = Q()

        for cambio_selecionado in cambios_selecionados:
            if cambio_selecionado is not None:
                lista_de_cambios.append(cambio_selecionado)

        for cambio in lista_de_cambios:
            filtro_cambios |= Q(cambio__nome_cambio=cambio)

        # Junção dos Filtros
        filtro.append(filtro_estados_de_conservacao)
        filtro.append(filtro_cores)
        filtro.append(filtro_marcas)
        filtro.append(filtro_cambios)

        qs = qs.filter(*filtro)

        return qs
