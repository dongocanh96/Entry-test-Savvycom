from rest_framework import serializers
from .models import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class InfoNopkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['price', 'marketCap']