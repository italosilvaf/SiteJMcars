# Generated by Django 4.0.6 on 2022-10-31 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_home_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='titulo_quadrado_grande_dois',
            field=models.CharField(default=' ', max_length=50, verbose_name='Título 2 do quadrado grande'),
        ),
        migrations.AlterField(
            model_name='home',
            name='titulo_quadrado_grande_tres',
            field=models.CharField(default=' ', max_length=50, verbose_name='Título 3 do quadrado grande'),
        ),
        migrations.AlterField(
            model_name='home',
            name='titulo_quadrado_grande_um',
            field=models.CharField(default=' ', max_length=50, verbose_name='Título 1 do quadrado grande '),
        ),
    ]
