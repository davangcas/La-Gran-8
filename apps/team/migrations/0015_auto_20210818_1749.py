# Generated by Django 3.2.6 on 2021-08-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0014_alter_team_delegated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='assists',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Asistencias'),
        ),
        migrations.AlterField(
            model_name='player',
            name='goals',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Goles'),
        ),
        migrations.AlterField(
            model_name='player',
            name='played',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Partidos Jugados'),
        ),
        migrations.AlterField(
            model_name='player',
            name='red_cards',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Tarjetas Rojas'),
        ),
        migrations.AlterField(
            model_name='player',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='player',
            name='yellow_cards',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Tarjetas Amarillas'),
        ),
    ]