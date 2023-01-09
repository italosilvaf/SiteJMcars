# Generated by Django 4.1.5 on 2023-01-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_about', models.CharField(default='About', max_length=50, verbose_name='Página')),
                ('titulo_about', models.CharField(default=None, max_length=50, verbose_name='Título')),
                ('imagem_about', models.ImageField(blank=True, null=True, upload_to='imagens_about/imagens_background', verbose_name='Background (1920x400)')),
                ('publicado_about', models.BooleanField(default=False, verbose_name='Publicado')),
                ('titulo_texto_about', models.CharField(default=None, max_length=50, verbose_name='Título do texto')),
                ('subtitulo_texto_about', models.CharField(default=None, max_length=50, verbose_name='Subtítulo do texto')),
                ('texto_about', models.TextField(default=None, max_length=100000, verbose_name='Texto')),
                ('imagem_texto_um_about', models.ImageField(default=None, upload_to='imagens_about/imagens_texto_um', verbose_name='Imagem do quadrado 1 (400x500)')),
                ('imagem_texto_dois_about', models.ImageField(default=None, upload_to='imagens_about/imagens_texto_dois', verbose_name='Imagem do quadrado 2 (400x500)')),
                ('imagem_texto_tres_about', models.ImageField(default=None, upload_to='imagens_about/imagens_texto_tres', verbose_name='Imagem do quadrado 3 (400x500)')),
                ('titulo_fotos_about', models.CharField(default=None, max_length=50, verbose_name='Título da Equipe de Funcionários')),
                ('subtitulo_fotos_about', models.CharField(default=None, max_length=50, verbose_name='Subtítulo da Equipe de Funcionários')),
            ],
            options={
                'verbose_name': 'Presonalização da página Sobre Nós',
                'verbose_name_plural': 'Presonalização da página Sobre Nós',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=' ', max_length=20, verbose_name='Nome')),
                ('cargo', models.CharField(blank=True, default=' ', max_length=20, null=True, verbose_name='Cargo')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado')),
                ('link_insta', models.CharField(blank=True, default=None, max_length=1000000, null=True, verbose_name='Link do Instagram')),
                ('link_whats', models.CharField(blank=True, default=None, max_length=1000000, null=True, verbose_name='Link do WhatsApp')),
                ('link_face', models.CharField(blank=True, default=None, max_length=1000000, null=True, verbose_name='Link do Facebook')),
                ('foto', models.ImageField(default=' ', upload_to='imagens_about/imagens_funcionarios', verbose_name='Foto (400x442)')),
            ],
        ),
    ]
