# Generated by Django 2.0.2 on 2018-05-28 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_remove_detallefactura_sub_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='estado_proceso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos.estadosFactura'),
        ),
    ]
