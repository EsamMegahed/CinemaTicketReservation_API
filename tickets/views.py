from http import HTTPStatus
from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.

# All Methods To Create View API

# [1] - Without Rest and no model query FBV
def no_rest_no_model(request):
    guests = {
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
    }
    return JsonResponse(guests,status=HTTPStatus.INTERNAL_SERVER_ERROR,safe=False)