# Generated by Django 4.0.5 on 2022-06-14 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion_envio', '0002_remove_direccionenvio_envio2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direccionenvio',
            name='default',
        ),
    ]
