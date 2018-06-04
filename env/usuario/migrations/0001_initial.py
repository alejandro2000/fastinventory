# Generated by Django 2.0.2 on 2018-05-09 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import usuario.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='estados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='perfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_perfil', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='user2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=usuario.models.up_load_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0, null=True)),
                ('width_field', models.IntegerField(default=0, null=True)),
                ('edad', models.IntegerField(default=0)),
                ('tarjetaCredito', models.IntegerField(default=0)),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('estado', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.estados')),
                ('perfil', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.perfiles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]