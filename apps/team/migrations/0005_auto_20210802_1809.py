# Generated by Django 3.1.13 on 2021-08-02 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_noticia'),
        ('team', '0004_auto_20210728_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='delegated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delegado', to='administration.administrator', verbose_name='Delegado'),
        ),
    ]
