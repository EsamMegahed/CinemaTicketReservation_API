from rest_framework import serializers
from .models import Movie,Guest,Reservation

class MoiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk','name','phone_number','reservation']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'