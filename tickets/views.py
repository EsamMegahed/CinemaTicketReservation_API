from http import HTTPStatus
from django.shortcuts import render
from django.http.response import JsonResponse
from.models import Guest,Movie,Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,filters
from .serializers import GuestSerializer,MoiveSerializer,ReservationSerializer
from rest_framework import generics,mixins,viewsets
# Create your views here.

# All Methods To Create View API

# [1] - Function Based View
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
    #POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

#3.2 Get PUT DELETE
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request,pk):

    try :
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    #PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
     #DELETE
    if request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# ---- Strat Class Based Views ----
  
# [4] - Class Based View
#4.1 GET POST
class CBV_List(APIView):
    #GET
    def get(self,request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests,many=True)
        return Response(serializer.data)
    #POST
    def post(self,request):
        serializer = GuestSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
#4.2 GET POST
class CBV_pk(APIView):
    def get_object(self,pk):
        try: 
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    def put(self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# [5] - Mixins List
#5.1 GET POST
class Mixinslist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
#5.1 GET Put DELETE
class MixinsPk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)


# [6] - Generics
#6.1 GET POST
class GenericsList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GenericsPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


# [7] - Viewsets
#7.1 GET POST Put DELETE
class ViewsetsGuest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class ViewsetsMovie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoiveSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie']

class ViewsetsReservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer



# [8] - find movie
@api_view(['Get'])
def find_movie(request):
    movie = Movie.objects.filter(movie = request.data['movie'],hall= request.data['hall'])
    serialzer = MoiveSerializer(movie,many=True)
    return Response(serialzer.data)


# [9] - Create New Reservation
@api_view(['POST'])
def new_reservation(request):
    movie = Movie.objects.get(movie = request.data['movie'],hall= request.data['hall'])
    guest = Guest()
    guest.name = request.data['name']
    guest.phone_number = request.data['phone_number']
    guest.save()

    reservation = Reservation()
    reservation.guest = guest
    reservation.moive = movie
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)