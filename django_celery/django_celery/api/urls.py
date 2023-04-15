from django.urls import path,include
from .views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile',ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
