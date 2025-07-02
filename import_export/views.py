from rest_framework import generics
from .models import ImportData, ExportData
from .serializers import ImportDataSerializer, ExportDataSerializer
from .permissions import IsAdminOrReadOnly

class ImportDataListCreateView(generics.ListCreateAPIView):
    queryset = ImportData.objects.all()
    serializer_class = ImportDataSerializer
    permission_classes = [IsAdminOrReadOnly]

class ImportDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImportData.objects.all()
    serializer_class = ImportDataSerializer
    permission_classes = [IsAdminOrReadOnly]

class ExportDataListCreateView(generics.ListCreateAPIView):
    queryset = ExportData.objects.all()
    serializer_class = ExportDataSerializer
    permission_classes = [IsAdminOrReadOnly]

class ExportDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExportData.objects.all()
    serializer_class = ExportDataSerializer
    permission_classes = [IsAdminOrReadOnly]
