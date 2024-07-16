
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, VehicleViewSet
from . import views


router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('login/' , views.user_login ,name ='login'),
    path('start_parking/<str:license_plate_number>/', views.start_parking_session, name='start_parking_session'),
    path('end_parking/<str:license_plate_number>/', views.end_parking_session, name='end_parking_session'),
    path('', include(router.urls)),
]