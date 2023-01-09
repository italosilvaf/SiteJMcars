from django.contrib import admin
from . models import Home


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_home', 'titulo_home',
                    'subtitulo_home', 'publicado_home')
    list_display_links = ('id', 'nome_home')
    list_editable = ('publicado_home',)


admin.site.register(Home, HomeAdmin)
