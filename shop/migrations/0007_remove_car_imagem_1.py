# Generated by Django 4.0.6 on 2023-01-16 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_car_imagem_10_remove_car_imagem_11_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='imagem_1',
        ),
    ]
