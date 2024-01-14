from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all() 
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated] 

