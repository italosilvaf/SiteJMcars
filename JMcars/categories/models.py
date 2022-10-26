from tabnanny import verbose
from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name='Categoria')
    imagem_categoria = models.ImageField(
        upload_to='imagens_categorias', blank=True, null=True, verbose_name='Imagem do quadrado na Home (400x250)')

    def __str__(self):
        return self.nome_categoria
