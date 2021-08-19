# Generated by Django 3.2.6 on 2021-08-18 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0017_leaguetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='hour_of_match',
            field=models.CharField(choices=[('00', '00:00'), ('01', '01:00'), ('02', '02:00'), ('03', '03:00'), ('04', '04:00'), ('05', '05:00'), ('06', '06:00'), ('07', '07:00'), ('08', '08:00'), ('09', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00'), ('23', '23:00')], default='16', max_length=2, verbose_name='Hora del partido'),
        ),
        migrations.AlterField(
            model_name='match',
            name='date_of_match',
            field=models.DateField(verbose_name='Fecha del partido'),
        ),
    ]
