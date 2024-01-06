import os
from dotenv import load_dotenv

load_dotenv()


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(os.getenv('ADMIN_URL'), admin.site.urls),
    path('users/', include('users.urls')),
    path('management/', include('management.urls')),
]
