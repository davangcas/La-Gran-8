# Generated by Django 3.2.6 on 2021-08-28 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0039_auto_20210827_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configtournament',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.tournament'),
        ),
    ]