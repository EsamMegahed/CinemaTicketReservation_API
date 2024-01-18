from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Movie(models.Model):
    hall = models.CharField(max_length = 30)
    movie = models.CharField(max_length = 30)
    date = models.DateField()

class Guest(models.Model):
    name = models.CharField(max_length = 50)
    phone_number = models.IntegerField()


class Post(models.Model):
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    body = models.TextField()

class Reservation(models.Model):
    guest = models.ForeignKey(Guest,on_delete = models.CASCADE,related_name = 'reservation')
    moive = models.ForeignKey(Movie,on_delete = models.CASCADE,related_name = 'reservation')

    def __str__(self) -> str:
        return self.guest.name + "  his reserve >> " + self.moive.movie

@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def tokencreate(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user = instance)