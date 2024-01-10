from django.urls import path
from hiring.views import DriverListCreateView, DriverRetrieveUpdateDestroyView


app_name = "hiring"

urlpatterns = [
    path('drivers/', DriverListCreateView.as_view()),
    path('driver/<int:pk>/', DriverRetrieveUpdateDestroyView.as_view())
]