# Generated by Django 4.1.9 on 2024-04-22 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0015_producto_disponible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=False, verbose_name='Disponibilidad del producto'),
        ),
    ]