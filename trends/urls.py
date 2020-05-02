from django.urls import path
from . import views
#from rest_framework import routers 
#from .views import StockAppViewSet




urlpatterns = [
    path('',views.home, name = "home"), 
    path('about', views.about, name="about"),
    path('api', views.api, name= "api"),
    path('api/trends/', views.StockAppCreate.as_view(), name = 'trends_chart'),
    ]

