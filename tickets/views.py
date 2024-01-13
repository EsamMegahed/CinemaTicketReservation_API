from http import HTTPStatus
from django.shortcuts import render
from django.http.response import JsonResponse
from.models import Guest,Movie,Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import GuestSerializer,MoiveSerializer,ReservationSerializer
# Create your views here.

# All Methods To Create View API


def no_rest_no_model(request):
    guests = [
        {
            'id':1,
            'Name':'Ahmed',
            'mobile':'123456',
        },
        {
            'id':2,
            'Name':'Esam',
            'mobile':'5456123',
        },
    ]
    response = JsonResponse(guests,safe=False)
    return response


# [2] - model data default django without rest
def no_rest_from_model(request):
    data = Guest.objects.all()
    respons ={
        'guests':list(data.values('name','phone_number'))
    }
    return JsonResponse(respons)


# [3] - Function Based View
#3.1 Get POST
@api_view(['GET','POST'])
def FBV_List(request):
    #GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests,many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#3.1 Get PUT DELETE
