# Generated by Django 4.0.5 on 2022-06-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0002_ordenes_orden_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenes',
            name='envio',
            field=models.IntegerField(default=15000),
        ),
    ]