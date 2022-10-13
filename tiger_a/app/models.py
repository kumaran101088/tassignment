from django.db import models

class Inventory(models.Model):
    store = models.CharField(max_length=3, blank=False, null=False)
    sku = models.CharField(max_length=8, blank=False, null=False)
    product = models.CharField(max_length=150, blank=False, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    date = models.DateField(blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Inventory'

    def __str__(self):
        return f'{self.store} - {self.product} - {str(self.price)}'
