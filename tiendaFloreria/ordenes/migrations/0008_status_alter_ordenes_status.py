# Generated by Django 4.0.5 on 2022-06-27 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0007_alter_ordenes_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ordenes',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ordenes.status'),
        ),
    ]
