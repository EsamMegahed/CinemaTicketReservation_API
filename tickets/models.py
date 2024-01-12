from django.db import models

# Create your models here.


class Movie(models.Model):
    hall = models.CharField(max_length = 30)
    movie = models.CharField(max_length = 30)
    date = models.DateField()

class Guest(models.Model):
    name = models.CharField(max_length = 50)
    phone_number = models.IntegerField()


class Reservation(models.Model):
    guest = models.ForeignKey(Guest,on_delete = models.CASCADE,related_name = 'reservation')
    moive = models.ForeignKey(Movie,on_delete = models.CASCADE,related_name = 'reservation')