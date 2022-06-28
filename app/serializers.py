from rest_framework import serializers
from .models import Talaba

class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'