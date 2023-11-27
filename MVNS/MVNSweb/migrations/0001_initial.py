# Generated by Django 4.2.7 on 2023-11-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('reading_time', models.TimeField(auto_now_add=True, verbose_name='Time')),
                ('motorist_first_name', models.CharField(max_length=255, verbose_name='Motorist First Name')),
                ('motorist_middle_initial', models.CharField(blank=True, max_length=2, verbose_name='Motorist Middle Initial')),
                ('motorist_last_name', models.CharField(max_length=255, verbose_name='Motorist Last Name')),
                ('plate_number', models.CharField(max_length=20, verbose_name='Plate No.')),
                ('db_calculated', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Calculated dB')),
                ('db_reading', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='dB Reading')),
                ('distance_reading', models.IntegerField(verbose_name='Distance')),
            ],
        ),
    ]