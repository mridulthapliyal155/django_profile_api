from django.urls import path,include
from rest_framework.routers import DefaultRouter
from places import views


router = DefaultRouter()
router.register('places',views.PlacesViewSet)

urlpatterns = [
    path('',include(router.urls))
]