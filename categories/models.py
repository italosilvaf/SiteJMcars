from tabnanny import verbose
from django.db import models


class EstadoDeConservacao(models.Model):
    nome_estado_de_conservacao = models.CharField(
        max_length=50, verbose_name='Estado de Conservacao')
    imagem_estado_de_conservacao = models.ImageField(
        upload_to='imagens_estado_de_conservacao', blank=True, null=True, verbose_name='Imagem do quadrado na Home (400x250)')

    def __str__(self):
        return self.nome_estado_de_conservacao


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self):
        return self.nome_categoria


class Marca(models.Model):
    nome_marca = models.CharField(max_length=50, verbose_name='Marca')

    def __str__(self):
        return self.nome_marca


class Cor(models.Model):
    nome_cor = models.CharField(max_length=50, verbose_name='Cor')

    def __str__(self):
        return self.nome_cor

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'


class Cambio(models.Model):
    nome_cambio = models.CharField(max_length=50, verbose_name='Câmbio')

    def __str__(self):
        return self.nome_cambio

    class Meta:
        verbose_name = 'Câmbio'
        verbose_name_plural = 'Câmbios'
