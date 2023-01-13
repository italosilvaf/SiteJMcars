from django.db import models


class Home(models.Model):

    nome_home = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='Home')
    titulo_home = models.CharField(
        max_length=15, verbose_name='Título',  blank=True, null=True, default=None)
    subtitulo_home = models.CharField(
        max_length=30, verbose_name='Subtítulo',  blank=True, null=True, default=None)
    descricao_home = models.TextField(
        max_length=65, verbose_name='Descrição', blank=True, null=True, default=None)
    publicado_home = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_home = models.ImageField(
        upload_to='imagens_home', blank=True, null=True, verbose_name='Background (1920x803)', default=None)

    def __str__(self):
        return self.nome_home

    class Meta:
        verbose_name = 'Presonalização da página Home'
        verbose_name_plural = 'Presonalização da página Home'


class QualidadesHome(models.Model):

    nome_qualidade = models.CharField(
        max_length=50, verbose_name='Qualidade', blank=False, null=False, default='')
    descricao_qualidade = models.TextField(
        max_length=100, verbose_name='Descrição da qualidade', blank=True, null=True, default=None)
    publicado_qualidade = models.BooleanField(
        verbose_name='Publicado', default=False)
    icon_qualidade = models.ImageField(upload_to='imagens_home/icon_qualidades',
                                       blank=False, verbose_name='Icon (75x75)', null=False, default=None)

    def __str__(self):
        return self.nome_qualidade

    class Meta:
        verbose_name = 'Qualidade'
        verbose_name_plural = 'Qualidades'
