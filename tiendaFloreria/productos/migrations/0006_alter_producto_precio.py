# Generated by Django 4.0.5 on 2022-06-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_producto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]