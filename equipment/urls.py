from django.urls import path
from .views import EquipmentListCreateView, EquipmentRetrieveUpdateDestroyView

urlpatterns = [
    path('', EquipmentListCreateView.as_view(), name='equipment-list-create'),
    path('<int:pk>/', EquipmentRetrieveUpdateDestroyView.as_view(), name='equipment-detail'),
]
