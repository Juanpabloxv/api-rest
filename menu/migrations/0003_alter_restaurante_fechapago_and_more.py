# Generated by Django 4.1.6 on 2023-02-13 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_restaurante_fechapago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='fechaPago',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='identificacionUsuario',
            field=models.IntegerField(),
        ),
    ]