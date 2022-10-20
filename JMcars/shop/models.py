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
