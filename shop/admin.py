from django.contrib import admin
from . models import Shop, Car, ImagesCar
from django_summernote.admin import SummernoteModelAdmin


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_shop', 'titulo_shop', 'publicado_shop')
    list_display_links = ('id', 'nome_shop')
    list_editable = ('publicado_shop',)


class ImagesCarInline(admin.TabularInline):
    model = ImagesCar
    extra = 1


class CarAdmin(SummernoteModelAdmin):
    list_display = ('id',  'modelo', 'cor', 'ano','get_quilometragem_formatado', 'get_preco_formatado', 'categoria', 'publicado')
    list_display_links = ('id', 'modelo')
    list_editable = ('publicado',)
    inlines = [
        ImagesCarInline
    ]


admin.site.register(Car, CarAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(ImagesCar)
