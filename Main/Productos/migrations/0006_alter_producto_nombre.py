# Generated by Django 4.2.6 on 2024-03-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(db_index=True, max_length=40, verbose_name='Nombre del Producto'),
        ),
    ]