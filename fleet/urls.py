from django.urls import path
from fleet.views import TruckListCreateAPIView, TruckRetrieveUpdateDestroyAPIView


app_name = "fleet"

urlpatterns = [
    path('trucks/', TruckListCreateAPIView.as_view()),
    path('truck/<int:pk>/', TruckRetrieveUpdateDestroyAPIView.as_view()),
]