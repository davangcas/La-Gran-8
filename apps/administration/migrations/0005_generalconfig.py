# Generated by Django 3.2.6 on 2021-08-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_noticia'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players_requisit', models.PositiveSmallIntegerField(blank=True, default=12, null=True, verbose_name='Cantidad de jugadores minima')),
            ],
            options={
                'verbose_name': 'Configuración General',
                'verbose_name_plural': 'Configuración General',
            },
        ),
    ]