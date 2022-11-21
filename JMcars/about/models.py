from email.policy import default
from django.db import models


class About(models.Model):

    nome_about = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_about = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    imagem_about = models.ImageField(
        upload_to='imagens_about/imagens_background', blank=False, null=False, verbose_name='Background (1920x400)')
    publicado_about = models.BooleanField(
        verbose_name='Publicado', default=False)
    titulo_texto_about = models.CharField(
        max_length=50, verbose_name='Título do texto',  blank=False, null=False, default=None)
    subtitulo_texto_about = models.CharField(
        max_length=50, verbose_name='Subtítulo do texto',  blank=False, null=False, default=None)
    texto_about = models.TextField(
        max_length=100000, verbose_name='Texto', blank=False, null=False, default=None)
    imagem_texto_um_about = models.ImageField(
        upload_to='imagens_about/imagens_texto_um', blank=False, null=False, default=None, verbose_name='Imagem do quadrado 1 (400x500)')
    imagem_texto_dois_about = models.ImageField(
        upload_to='imagens_about/imagens_texto_dois', blank=False, null=False, default=None, verbose_name='Imagem do quadrado 2 (400x500)')
    imagem_texto_tres_about = models.ImageField(
        upload_to='imagens_about/imagens_texto_tres', blank=False, null=False, default=None, verbose_name='Imagem do quadrado 3 (400x500)')
    titulo_fotos_about = models.CharField(
        max_length=50, verbose_name='Título da Equipe de Funcionários',  blank=False, null=False, default=None)
    subtitulo_fotos_about = models.CharField(
        max_length=50, verbose_name='Subtítulo da Equipe de Funcionários',  blank=False, null=False, default=None)

    def __str__(self):
        return self.nome_about

    class Meta:
        verbose_name = 'Presonalização da página Sobre Nós'
        verbose_name_plural = 'Presonalização da página Sobre Nós'


class Funcionario(models.Model):

    nome = models.CharField(
        max_length=20, verbose_name='Nome', blank=False, null=False, default=' ')
    cargo = models.CharField(
        max_length=20, verbose_name='Cargo', blank=True, null=True, default=' ')
    publicado = models.BooleanField(
        verbose_name='Publicado', default=False)
    link_insta = models.CharField(max_length=1000000, verbose_name='Link do Instagram',
                                  blank=True, null=True, default=None)
    link_whats = models.CharField(max_length=1000000, verbose_name='Link do WhatsApp',
                                  blank=True, null=True, default=None)
    link_face = models.CharField(max_length=1000000, verbose_name='Link do Facebook',
                                 blank=True, null=True, default=None)
    foto = models.ImageField(upload_to='imagens_about/imagens_funcionarios',
                             blank=False, null=False, default=' ', verbose_name='Foto (400x442)')

    def __str__(self):
        return self.nome
