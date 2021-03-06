# Generated by Django 3.1.7 on 2021-07-28 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_delegated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='drawn',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Partidos Empatados'),
        ),
        migrations.AlterField(
            model_name='team',
            name='lost',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Partidos Perdidos'),
        ),
        migrations.AlterField(
            model_name='team',
            name='titles',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Títulos conseguidos'),
        ),
        migrations.AlterField(
            model_name='team',
            name='win',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Partidos Ganados'),
        ),
    ]
