from rest_framework import serializers 
from trends.models import StockApp

class StockAppSerializer(serializers.ModelSerializer):
    class Meta: 
        model = StockApp
        fields = '__all__'