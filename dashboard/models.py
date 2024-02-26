from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}'