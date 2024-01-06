from django.urls import path
from users import views


urlpatterns = [
    path('set-password/<str:verification_link>/')
]