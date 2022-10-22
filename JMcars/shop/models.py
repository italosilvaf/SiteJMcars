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
        max_length=50, verbose_name='Modelo', default=None)
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
    imagem_um = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=False, null=False, default=None, verbose_name='Imagem 1 (Capa)')
    imagem_dois = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 2')
    imagem_tres = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 3')
    imagem_quatro = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 4')
    imagem_cinco = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 4')
    imagem_seis = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 6')
    imagem_sete = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 7')
    imagem_oito = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 8')
    imagem_nove = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 9')
    imagem_dez = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 10')

    def __str__(self):
        return self.modelo
