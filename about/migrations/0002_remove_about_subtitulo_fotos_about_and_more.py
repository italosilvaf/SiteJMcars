# Generated by Django 4.1.5 on 2023-01-13 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='subtitulo_fotos_about',
        ),
        migrations.RemoveField(
            model_name='about',
            name='titulo_fotos_about',
        ),
    ]