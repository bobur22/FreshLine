from rest_framework import serializers
from .models import ImportData, ExportData

class ImportDataSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ImportData
        fields = ['id', 'product', 'product_name', 'country', 'volume', 'price', 'description']

class ExportDataSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ExportData
        fields = ['id', 'product', 'product_name', 'target_country', 'demand_level', 'description']

