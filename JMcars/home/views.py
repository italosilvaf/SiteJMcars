from categories.models import Categoria
from .models import Home
from django.views.generic.list import ListView


class Index(ListView):
    model = Home
    template_name = 'home/index.html'
    context_object_name = 'valores'

    def get_queryset(self):
        valor = Home.objects.filter(publicado_home=True).order_by('-id')[:1]
        return valor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
