from django.urls import path, include

from rest_framework.routers import DefaultRouter

from maintenance.views import StatusViewset

router = DefaultRouter()
router.register(r'status', StatusViewset, basename='status')



app_name = "maintenance"

urlpatterns = [
    path('', include(router.urls))
]
