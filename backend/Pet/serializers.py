from rest_framework import serializers
from Pet.models import Pet,Account


class PetSerializer(serializers.ModelSerializer):
    # comments = serializers.ListField()
    class Meta:
        model=Pet
        fields='__all__'
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'