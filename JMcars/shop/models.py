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
    imagem_1 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=False, null=False, default=None, verbose_name='Imagem 1 (Capa)')
    imagem_2 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 2')
    imagem_3 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 3')
    imagem_4 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 4')
    imagem_5 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 5')
    imagem_6 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 6')
    imagem_7 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 7')
    imagem_8 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 8')
    imagem_9 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 9')
    imagem_10 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 10')
    imagem_11 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 11')
    imagem_12 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 12')
    imagem_13 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 13')
    imagem_14 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 14')
    imagem_15 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 15')
    imagem_16 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 16')
    imagem_17 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 17')
    imagem_18 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 18')
    imagem_19 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 19')
    imagem_20 = models.ImageField(
        upload_to='imagens_shop/imagens_carros', blank=True, null=True, verbose_name='Imagem 20')

    def __str__(self):
        return self.modelo
