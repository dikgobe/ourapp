from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet ,UserView,UserLoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("get_user/", UserView.as_view()),
    path("login/" , UserLoginView.as_view()),
 
]
