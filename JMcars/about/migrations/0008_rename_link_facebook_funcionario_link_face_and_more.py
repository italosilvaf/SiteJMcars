# Generated by Django 4.0.6 on 2022-10-31 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_alter_funcionario_cargo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='link_facebook',
            new_name='link_face',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='link_instagram',
            new_name='link_insta',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='link_whatsapp',
            new_name='link_whats',
        ),
    ]
