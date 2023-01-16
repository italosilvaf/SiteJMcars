from django.db import models
from categories.models import Categoria, Marca, Cor, Cambio
from utils import utils


class Shop(models.Model):

    nome_shop = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_shop = models.CharField(
        max_length=40, verbose_name='Título',  blank=True, null=True, default=None)
    imagem_shop = models.ImageField(
        upload_to='imagens_shop/imagens_background', blank=True, null=True, default=None, verbose_name='Background (1920x400)')
    publicado_shop = models.BooleanField(
        verbose_name='Publicado', default=False)

    def __str__(self):
        return self.nome_shop

    class Meta:
        verbose_name = 'Presonalização da página Estoque'
        verbose_name_plural = 'Presonalização da página Estoque'


class Car(models.Model):

    modelo = models.CharField(
        max_length=100, verbose_name='Modelo', default=None)
    marca = models.ForeignKey(
        Marca, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Marca')
    ano = models.CharField(max_length=9, verbose_name='Ano', default=None)
    cor = models.ForeignKey(
        Cor, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Cor')
    quilometragem = models.PositiveIntegerField(
        verbose_name='Quilometragem', blank=False, null=False)
    motorizacao = models.CharField(
        max_length=20, verbose_name='Motorização', default=None)
    cambio = models.ForeignKey(
        Cambio, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Câmbio')
    preco = models.FloatField(verbose_name='Preço',
                              default='0', blank=False, null=False)
    categoria_carro = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Categoria')
    opcionais = models.TextField(
        verbose_name='Opcionais', blank=True, null=True)
    publicado = models.BooleanField(
        verbose_name='Publicado', default=False)

    def get_preco_formatado(self):
        return utils.formata_preco_admin(self.preco)
    get_preco_formatado.short_description = "Preço"

    def get_quilometragem_formatado(self):
        return utils.formata_quilometragem(self.quilometragem)
    get_quilometragem_formatado.short_description = "Quilometragem"

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'


class ImagesCar(models.Model):

    carro = models.ForeignKey(Car, on_delete=models.CASCADE)
    imagem = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=False, null=False, default=None, verbose_name='Imagem')

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
