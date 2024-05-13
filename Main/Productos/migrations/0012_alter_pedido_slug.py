# Generated by Django 4.1.9 on 2024-04-21 22:48

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0011_pedido_slug_alter_pedido_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='nombre', unique=True),
        ),
    ]
