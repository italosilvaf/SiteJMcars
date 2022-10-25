from django.db import models


class Shop(models.Model):

    nome_shop = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_shop = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    imagem_shop = models.ImageField(
        upload_to='imagens_shop/imagens_background', blank=True, null=True, verbose_name='Background')
    publicado_shop = models.BooleanField(
        verbose_name='Publicado', default=False)

    def __str__(self):
        return self.nome_shop


class Car(models.Model):

    modelo = models.CharField(
        max_length=100, verbose_name='Modelo', default=None)
    marca = models.CharField(
        max_length=50, verbose_name='Marca', default=None)
    ano = models.CharField(max_length=9, verbose_name='Ano', default=None)
    cor = models.CharField(max_length=50, verbose_name='Cor', default=None)
    quilometragem = models.CharField(
        max_length=50, verbose_name='Quilometragem', default=None)
    motorizacao = models.CharField(
        max_length=50, verbose_name='Motorização', default=None)
    cambio = models.CharField(
        max_length=50, verbose_name='Câmbio', default=None)
    preco = models.CharField(
        max_length=50, verbose_name='Preço', default=None)
    publicado = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_capa = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=False, null=False, default=None, verbose_name='Imagem 1 (Capa)')

    def __str__(self):
        return self.modelo
