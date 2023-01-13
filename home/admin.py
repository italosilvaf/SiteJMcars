from django.contrib import admin
from . models import Home, QualidadesHome


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_home', 'titulo_home',
                    'subtitulo_home', 'publicado_home')
    list_display_links = ('id', 'nome_home')
    list_editable = ('publicado_home',)


admin.site.register(Home, HomeAdmin)


class QualidadesHomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_qualidade',
                    'descricao_qualidade', 'publicado_qualidade')
    list_display_links = ('id', 'nome_qualidade')
    list_editable = ('publicado_qualidade',)


admin.site.register(QualidadesHome, QualidadesHomeAdmin)
