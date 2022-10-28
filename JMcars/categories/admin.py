from django.contrib import admin
from .models import Categoria, Marca, Cor, Cambio


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    list_display_links = ('id', 'nome_categoria')


admin.site.register(Categoria, CategoriaAdmin)


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_marca')
    list_display_links = ('id', 'nome_marca')


admin.site.register(Marca, MarcaAdmin)


class CorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cor')
    list_display_links = ('id', 'nome_cor')


admin.site.register(Cor, CorAdmin)


class CambioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cambio')
    list_display_links = ('id', 'nome_cambio')


admin.site.register(Cambio, CambioAdmin)
