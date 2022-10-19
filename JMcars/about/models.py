from django.db import models


class About(models.Model):

    nome_about = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_about = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    subtitulo_about = models.TextField(
        max_length=50, verbose_name='Subtítulo',  blank=True, null=True, default=None)
    descricao_about = models.TextField(
        max_length=500, verbose_name='Descrição', blank=False, null=True, default=None)
    publicado_about = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_about = models.ImageField(
        upload_to='imagens_about/imagens_background', blank=True, null=True, verbose_name='Background')
    imagem_quadrado_um = models.ImageField(
        upload_to='imagens_about/imagens_texto_um', blank=True, null=True, verbose_name='Imagem do texto 1')
    imagem_quadrado_dois = models.ImageField(
        upload_to='imagens_about/imagens_texto_dois', blank=True, null=True, verbose_name='Imagem do texto 2')
    imagem_quadrado_tres = models.ImageField(
        upload_to='imagens_about/imagens_texte_tres', blank=True, null=True, verbose_name='Imagem do texto 3')

    def __str__(self):
        return self.nome_pagina
