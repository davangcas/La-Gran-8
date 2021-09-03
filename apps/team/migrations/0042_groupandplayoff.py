# Generated by Django 3.2.6 on 2021-09-03 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0041_player_dorsal'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupAndPlayOff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('away_goal', models.BooleanField(default=True, verbose_name='Gol de Visitante')),
                ('teams_second_round', models.PositiveSmallIntegerField(default=2, verbose_name='Cantidad de equipos que clasifican a segunda ronda')),
                ('groups', models.PositiveSmallIntegerField(default=8, verbose_name='Cantidad de grupos')),
                ('tournament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.tournament')),
            ],
            options={
                'verbose_name': 'Grupo y Eliminatoria - Configuración',
                'verbose_name_plural': 'Grupo y Eliminatoria - Configuraciones',
            },
        ),
    ]
