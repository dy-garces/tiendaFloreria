# Generated by Django 4.0.5 on 2022-06-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_carrito_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritoproductos',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]
