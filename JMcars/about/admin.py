from django.contrib import admin
from . models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_about', 'titulo_about', 'publicado_about')
    list_display_links = ('id', 'nome_about')
    list_editable = ('publicado_about',)


admin.site.register(About, AboutAdmin)
