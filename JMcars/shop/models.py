from django.db import models
from categories.models import Categoria, Marca, Cor, Cambio


class Shop(models.Model):

    nome_shop = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_shop = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    imagem_shop = models.ImageField(
        upload_to='imagens_shop/imagens_background', blank=False, null=False, default=None, verbose_name='Background (1920x400)')
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
    quilometragem = models.CharField(max_length=50,
                                     verbose_name='Quilometragem', blank=False, null=False)
    motorizacao = models.CharField(
        max_length=50, verbose_name='Motorização', default=None)
    cambio = models.ForeignKey(
        Cambio, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Câmbio')
    preco = models.CharField(max_length=50, verbose_name='Preço',
                             default='0', blank=False, null=False)
    categoria_carro = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Categoria')
    opcionais = models.TextField(
        verbose_name='Opcionais', blank=True, null=True)
    publicado = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_1 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=False, null=False, default=None, verbose_name='Imagem 1 (Capa)')
    imagem_2 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 2', default=None)
    imagem_3 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 3', default=None)
    imagem_4 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 4', default=None)
    imagem_5 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 5', default=None)
    imagem_6 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 6', default=None)
    imagem_7 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 7', default=None)
    imagem_8 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 8', default=None)
    imagem_9 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 9', default=None)
    imagem_10 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 10', default=None)
    imagem_11 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 11', default=None)
    imagem_12 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 12', default=None)
    imagem_13 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 13', default=None)
    imagem_14 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 14', default=None)
    imagem_15 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 15', default=None)
    imagem_16 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 16', default=None)
    imagem_17 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 17', default=None)
    imagem_18 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 18', default=None)
    imagem_19 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 19', default=None)
    imagem_20 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 20', default=None)

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
