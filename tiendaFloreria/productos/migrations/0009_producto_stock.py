# Generated by Django 4.0.5 on 2022-06-25 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_producto_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]