from django.db import models


class Home(models.Model):

    nome_home = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='Home')
    titulo_home = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    subtitulo_home = models.CharField(
        max_length=50, verbose_name='Subtítulo',  blank=True, null=True, default=None)
    descricao_home = models.TextField(
        max_length=250, verbose_name='Descrição', blank=True, null=True, default=None)
    publicado_home = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_home = models.ImageField(
        upload_to='imagens_home/background_header', blank=False, null=False, verbose_name='Background (1920x803)', default=None)
    titulo_quadrado_grande_um = models.CharField(
        max_length=50, verbose_name='Título 1 do quadrado grande ', blank=True, null=True, default=' ')
    descricao_quadrado_grande_um = models.TextField(
        max_length=100, verbose_name='Descrição 1 do quadrado grande ', blank=True, null=True, default=None)
    titulo_quadrado_grande_dois = models.CharField(
        max_length=50, verbose_name='Título 2 do quadrado grande', blank=True, null=True, default=' ')
    descricao_quadrado_grande_dois = models.TextField(
        max_length=100, verbose_name='Descrição 2 do quadrado grande ', blank=True, null=True, default=None)
    titulo_quadrado_grande_tres = models.CharField(
        max_length=50, verbose_name='Título 3 do quadrado grande', blank=True, null=True, default=' ')
    descricao_quadrado_grande_tres = models.TextField(
        max_length=100, verbose_name='Descrição 3 do quadrado grande ', blank=True, null=True, default=None)

    def __str__(self):
        return self.nome_home
