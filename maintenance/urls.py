from django.urls import path, include

from rest_framework.routers import DefaultRouter

from maintenance.views import (
    StatusViewset, CaseListCreateView, 
    CaseRetrieveUpdateDestroyView, NoteViewSet,
    OdodmeteRetrieveUpdateDestroyView, OdodmeterListCreateView,
    ServiceViewSet,
)

router = DefaultRouter()
router.register(r'status', StatusViewset, basename='status')
router.register(r'note', NoteViewSet, basename='note')
router.register(r'service', ServiceViewSet, basename='service')



app_name = "maintenance"

urlpatterns = [
    path('', include(router.urls)),
    path('case/', CaseListCreateView.as_view()),
    path('case/<int:pk>/', CaseRetrieveUpdateDestroyView.as_view()),
    path('ododmeter/', OdodmeterListCreateView.as_view()),
    path('ododmeter/<int:pk>/', OdodmeteRetrieveUpdateDestroyView.as_view()),
]
