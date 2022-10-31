from django.contrib import admin
from . models import Shop
from . models import Car
from django_summernote.admin import SummernoteModelAdmin


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_shop', 'titulo_shop', 'publicado_shop')
    list_display_links = ('id', 'nome_shop')
    list_editable = ('publicado_shop',)


admin.site.register(Shop, ShopAdmin)


class CarAdmin(SummernoteModelAdmin):
    list_display = ('id',  'modelo', 'cor', 'ano',
                    'quilometragem', 'preco', 'publicado')
    list_display_links = ('id', 'modelo')
    list_editable = ('publicado',)


admin.site.register(Car, CarAdmin)
