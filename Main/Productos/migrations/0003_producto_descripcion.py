# Generated by Django 4.1.9 on 2024-04-06 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_remove_detallepedido_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]