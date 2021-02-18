from rest_framework import serializers
from restapi.models import superstore

class StatSerializer(serializers.Serializer):
    segment = serializers.CharField(max_length=25, required=True)
    sales = serializers.DecimalField(max_digits=12, decimal_places=5, required=True)
    profit = serializers.DecimalField(max_digits=12, decimal_places=5, required=True)

    class Meta:
        fields = ('segment', 'sale', 'profit')
