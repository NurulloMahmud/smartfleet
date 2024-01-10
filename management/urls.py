from django.urls import path
from management.views import CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView


app_name = "management"

urlpatterns = [
    path('carriers/', CompanyListCreateAPIView.as_view()),
    path('carrier/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view()),
]