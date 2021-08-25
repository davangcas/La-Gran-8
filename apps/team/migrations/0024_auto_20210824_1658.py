# Generated by Django 3.2.6 on 2021-08-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0023_league_vueltas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playoff',
            name='initial_round',
        ),
        migrations.AddField(
            model_name='playoff',
            name='away_goal',
            field=models.BooleanField(default=True, verbose_name='Gol de visitante'),
        ),
        migrations.AlterField(
            model_name='fieldmatch',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Cancha'),
        ),
        migrations.DeleteModel(
            name='TeamLeague',
        ),
    ]