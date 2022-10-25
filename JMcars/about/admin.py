from django.contrib import admin
from . models import About
from . models import Funcionario


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_about', 'titulo_about', 'publicado_about')
    list_display_links = ('id', 'nome_about')
    list_editable = ('publicado_about',)


admin.site.register(About, AboutAdmin)


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargo', 'publicado')
    list_display_links = ('id', 'nome')
    list_editable = ('publicado',)


admin.site.register(Funcionario, FuncionarioAdmin)
