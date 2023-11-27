from django.db import models

# Create your models here.

class Reading(models.Model):
    reading_date = models.DateField(auto_now_add=True, verbose_name='Date')
    reading_time = models.TimeField(auto_now_add=True, verbose_name='Time')
    motorist_first_name = models.CharField(max_length=255, verbose_name='Motorist First Name')
    motorist_middle_initial = models.CharField(max_length=2, blank=True, verbose_name='Motorist Middle Initial')
    motorist_last_name = models.CharField(max_length=255, verbose_name='Motorist Last Name')
    plate_number = models.CharField(max_length=20, verbose_name='Plate No.')
    db_calculated = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Calculated dB')
    db_reading = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='dB Reading')
    distance_reading = models.IntegerField(verbose_name='Distance')
    
    def __str__(self):
        return (self.motorist_first_name + ' ' + self.motorist_middle_initial + ' ' + self.motorist_last_name)
    
    def primary_key(self):
        print (self.pk)
        return self.pk