from django.urls import path
from .views import (
    ImportDataListCreateView,
    ImportDataRetrieveUpdateDestroyView,
    ExportDataListCreateView,
    ExportDataRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('import/', ImportDataListCreateView.as_view(), name='import-list-create'),
    path('import/<int:pk>/', ImportDataRetrieveUpdateDestroyView.as_view(), name='import-detail'),
    path('export/', ExportDataListCreateView.as_view(), name='export-list-create'),
    path('export/<int:pk>/', ExportDataRetrieveUpdateDestroyView.as_view(), name='export-detail'),
]
