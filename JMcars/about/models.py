from django.db import models

# Create your models here.
from django.db import models


class About(models.Model):

    nome_about = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_about = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    imagem_about = models.ImageField(
        upload_to='imagens_about/imagens_background', blank=True, null=True, verbose_name='Background (1920x400)')
    publicado_about = models.BooleanField(
        verbose_name='Publicado', default=False)
    titulo_texto_about = models.CharField(
        max_length=50, verbose_name='Título do texto',  blank=True, null=True, default=None)
    subtitulo_texto_about = models.CharField(
        max_length=50, verbose_name='Subtítulo do texto',  blank=True, null=True, default=None)
    texto_about = models.TextField(
        max_length=100000, verbose_name='Texto', blank=True, null=True, default=None)
    imagem_texto_um_about = models.ImageField(
        upload_to='imagens_about/imagens_texto_um', blank=True, null=True, verbose_name='Imagem do quadrado 1 (400x500)')
    imagem_texto_dois_about = models.ImageField(
        upload_to='imagens_about/imagens_texto_dois', blank=True, null=True, verbose_name='Imagem do quadrado 2 (400x500)')
    imagem_texto_tres_about = models.ImageField(
        upload_to='imagens_about/imagens_texto_tres', blank=True, null=True, verbose_name='Imagem do quadrado 3 (400x500)')
    titulo_fotos_about = models.CharField(
        max_length=50, verbose_name='Título das Fotos',  blank=True, null=True, default=None)
    subtitulo_fotos_about = models.TextField(
        max_length=50, verbose_name='Subtítulo das Fotos',  blank=True, null=True, default=None)

    def __str__(self):
        return self.nome_about


class Funcionario(models.Model):

    nome = models.CharField(
        max_length=20, verbose_name='Nome', blank=False, null=False, default=' ')
    cargo = models.CharField(
        max_length=20, verbose_name='Cargo', blank=False, null=False, default=' ')
    publicado = models.BooleanField(
        verbose_name='Publicado', default=False)
    link_instagram = models.CharField(max_length=1000000, verbose_name='Link do Instagram',
                                      blank=True, null=True, default=None)
    link_whatsapp = models.CharField(max_length=1000000, verbose_name='Link do WhatsApp',
                                     blank=True, null=True, default=None)
    link_facebook = models.CharField(max_length=1000000, verbose_name='Link do Facebook',
                                     blank=True, null=True, default=None)
    foto = models.ImageField(upload_to='imagens_about/imagens_funcionarios',
                             blank=True, null=True, verbose_name='Foto (400x442)')

    def __str__(self):
        return self.nome
