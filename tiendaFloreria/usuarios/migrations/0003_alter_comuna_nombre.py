# Generated by Django 4.0.5 on 2022-06-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_region_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='nombre',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]