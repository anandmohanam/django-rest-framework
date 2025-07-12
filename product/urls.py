from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, RegisterView, LoginView, ReviewViewSet, LogoutView

# from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('', include(router.urls)),
]
