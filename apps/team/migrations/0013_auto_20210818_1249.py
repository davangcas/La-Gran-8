# Generated by Django 3.2.6 on 2021-08-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_auto_20210818_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='teams',
        ),
        migrations.AddField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(related_name='tournament_teams', to='team.Team', verbose_name='Equipos del torneo'),
        ),
    ]
