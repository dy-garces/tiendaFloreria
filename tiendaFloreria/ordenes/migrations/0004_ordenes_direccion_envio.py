# Generated by Django 4.0.5 on 2022-06-14 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion_envio', '0003_remove_direccionenvio_default'),
        ('ordenes', '0003_ordenes_envio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenes',
            name='direccion_envio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='direccion_envio.direccionenvio'),
        ),
    ]