# Generated by Django 2.0.2 on 2018-05-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20180514_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='user2',
            name='direccion',
            field=models.CharField(default='colombia', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user2',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
    ]
