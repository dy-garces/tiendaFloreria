# Generated by Django 4.0.5 on 2022-06-12 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='producto',
            new_name='productos',
        ),
    ]
