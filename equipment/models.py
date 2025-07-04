from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='equipment/', blank=True, null=True)

    def __str__(self):
        return self.name