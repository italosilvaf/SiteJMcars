# Generated by Django 4.1.5 on 2023-01-19 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='categoria_carro',
            new_name='categoria',
        ),
    ]