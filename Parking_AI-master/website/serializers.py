from rest_framework import serializers
from .models import Profile, Vehicle,ParkingSession

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

# class ParkingSessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ParkingSession
#         fields = '__all__'