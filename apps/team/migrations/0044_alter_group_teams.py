# Generated by Django 3.2.6 on 2021-09-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0043_group_grouptable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teams',
            field=models.ManyToManyField(blank=True, null=True, to='team.Team'),
        ),
    ]
