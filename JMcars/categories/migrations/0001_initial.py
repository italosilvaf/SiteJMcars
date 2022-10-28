# Generated by Django 4.0.6 on 2022-10-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cambio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cambio', models.CharField(max_length=50, verbose_name='Câmbio')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=50, verbose_name='Categoria')),
                ('imagem_categoria', models.ImageField(blank=True, null=True, upload_to='imagens_categorias', verbose_name='Imagem do quadrado na Home (400x250)')),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cor', models.CharField(max_length=50, verbose_name='Cor')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_marca', models.CharField(max_length=50, verbose_name='Marca')),
            ],
        ),
    ]
