from django.db import models
from products.models import Product

class ImportData(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='import_entries'
    )
    country = models.CharField(max_length=255)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Import: {self.product.name} from {self.country}"

class ExportData(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='export_entries'
    )
    target_country = models.CharField(max_length=255)
    demand_level = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Export: {self.product.name} to {self.target_country}"
