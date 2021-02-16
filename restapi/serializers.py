from rest_framework import serializers
from.models import superstore

class storeSerializer(serializers.ModelSerializer):

    class Meta:
        model = superstore
        fields = '__all__'