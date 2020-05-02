#from rest_framework import viewsets, permissions 
#from rest_framework.views import ListCreateAPIView
from django.shortcuts import render
from .models import StockApp
from django.http import JsonResponse
from .serializers import StockAppSerializer
from rest_framework import generics


#StockApp Viewsets
#class StockAppViewSet(viewsets.ModelViewSet):
 #   queryset = StockApp.objects.all()
  #  permission_classes= []
   # serializer_class = StockAppSerializer

class StockAppCreate(generics.ListCreateAPIView):
   queryset = StockApp.objects.all()
   serializer_class = StockAppSerializer

 # Create your views here.
def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request, 'about.html',{})

def api(request):
    return render(request, 'api.html',{})

def trends_chart(request):
    labels =[]
    data =[]

    queryset = StockApp.objects.all()
    for entry in querset: 
        labels.labels
        data.data

    return JsonResponse(data ={
        'labels':labels,
        'data':data,
    })

   # return render(request, 'api.html',{