# Generated by Django 4.1.3 on 2022-11-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_home_imagem_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='imagem_home',
            field=models.ImageField(default=None, upload_to='imagens_home', verbose_name='Background (1920x803)'),
        ),
    ]