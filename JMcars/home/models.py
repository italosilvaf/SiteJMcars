from django.db import models


class Home(models.Model):

    nome_home = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='Home')
    titulo_home = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    subtitulo_home = models.TextField(
        max_length=50, verbose_name='Subtítulo',  blank=True, null=True, default=None)
    descricao_home = models.TextField(
        max_length=250, verbose_name='Descrição', blank=True, null=True, default=None)
    publicado_home = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_home = models.ImageField(
        upload_to='imagens_home/background/header', blank=False, null=False, verbose_name='Background (1920x803)', default=None)
    titulo_quadrado_um = models.CharField(
        max_length=50, verbose_name='Título do quadrado 1', blank=True, null=True, default=' ')
    imagem_quadrado_um = models.ImageField(
        upload_to='imagens_home/quadrado1', blank=True, null=True, verbose_name='Imagem do quadrado 1 (400x250)')
    titulo_quadrado_dois = models.CharField(
        max_length=50, verbose_name='Título do quadrado 2', blank=True, null=True, default=' ')
    imagem_quadrado_dois = models.ImageField(
        upload_to='imagens_home/quadrado2', blank=True, null=True, verbose_name='Imagem do quadrado 2 (400x250)')
    titulo_quadrado_tres = models.CharField(
        max_length=50, verbose_name='Título do quadrado 3', blank=True, null=True, default=' ')
    imagem_quadrado_tres = models.ImageField(
        upload_to='imagens_home/quadrado3', blank=True, null=True, verbose_name='Imagem do quadrado 3 (400x250)')
    titulo_quadrado_grande_um = models.CharField(
        max_length=50, verbose_name='Título 1 do quadrado grande ', blank=True, null=True, default=' ')
    descricao_quadrado_grande_um = models.TextField(
        max_length=250, verbose_name='Descrição 1 do quadrado grande ', blank=True, null=True, default=None)
    titulo_quadrado_grande_dois = models.CharField(
        max_length=50, verbose_name='Título 2 do quadrado grande', blank=True, null=True, default=' ')
    descricao_quadrado_grande_dois = models.TextField(
        max_length=250, verbose_name='Descrição 2 do quadrado grande ', blank=True, null=True, default=None)
    titulo_quadrado_grande_tres = models.CharField(
        max_length=50, verbose_name='Título 3 do quadrado grande', blank=True, null=True, default=' ')
    descricao_quadrado_grande_tres = models.TextField(
        max_length=250, verbose_name='Descrição 3 do quadrado grande ', blank=True, null=True, default=None)
    imagem_final_home = models.ImageField(
        upload_to='imagens_home/background/footer', blank=True, null=True, verbose_name='Imagem do final da página (1920x803)')
    titulo_final_home = models.CharField(
        max_length=50, verbose_name='Título do final da página', blank=True, null=True, default=' ')
    subtitulo_final_home = models.CharField(
        max_length=50, verbose_name='Subtitulo do final da página', blank=True, null=True, default=' ')
    conteudo_botao_home = models.CharField(
        max_length=50, verbose_name='Conteudo do botão do final da página', blank=True, null=True, default=' ')
    link_botao_home = models.CharField(
        max_length=1000, verbose_name='Link do botão do final da página', blank=True, null=True, default=' ')

    def __str__(self):
        return self.nome_home
