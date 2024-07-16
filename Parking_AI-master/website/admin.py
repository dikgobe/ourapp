from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile, Vehicle, ParkingSession

# Get the User model
User = get_user_model()

# Unregister the default User admin if it is already registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'license_plate_number', 'city', 'cellphone_number', 'private_profile')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('profile', 'reg_number', 'car_make', 'car_model')

@admin.register(ParkingSession)
class ParkingSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time')
