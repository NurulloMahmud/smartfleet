from rest_framework.routers import DefaultRouter

from django.urls import path, include
from fleet.views import TruckListCreateAPIView, TruckRetrieveUpdateDestroyAPIView, \
                        TruckInUseViewSet


router = DefaultRouter()
router.register(r'in-use', TruckInUseViewSet, basename='in-use')


app_name = "fleet"

urlpatterns = [
    path('trucks/', TruckListCreateAPIView.as_view()),
    path('truck/<int:pk>/', TruckRetrieveUpdateDestroyAPIView.as_view()),
    path('', include(router.urls))
]