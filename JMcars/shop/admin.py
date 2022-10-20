from django.contrib import admin
from . models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_shop', 'titulo_shop', 'publicado_shop')
    list_display_links = ('id', 'nome_shop')
    list_editable = ('publicado_shop',)


admin.site.register(Shop, ShopAdmin)
