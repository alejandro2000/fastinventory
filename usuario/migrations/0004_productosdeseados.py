# Generated by Django 2.0.2 on 2018-05-21 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20180515_0955'),
        ('usuario', '0003_auto_20180515_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='productosdeseados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('id_user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.user2')),
            ],
        ),
    ]
