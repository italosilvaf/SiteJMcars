from django.views.generic.list import ListView
from .models import About
from .models import Funcionario
from categories.models import Categoria


class Index(ListView):
    model = About
    template_name = 'about/index.html'
    context_object_name = 'valores'

    def get_queryset(self):
        valor = About.objects.filter(publicado_about=True).order_by('-id')[:1]
        return valor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.filter(
            publicado=True).order_by('id')
        context['categorias'] = Categoria.objects.all()
        return context
