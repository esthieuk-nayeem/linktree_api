from django.db import models
from authentication.models import User

# Create your models here.

class VendorModel(models.Model):
    name = models.CharField(null=False, max_length=250)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"

class ProductModel(models.Model):
    title = models.CharField(null=False, max_length=250)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=4, null=False)  # Changed to DecimalField
    location = models.CharField(null=False, max_length=250)
    capacity = models.CharField(null=False, max_length=250)
    link = models.CharField(null=True, blank=True, max_length=250)
    created_at = models.DateField(auto_now_add=True)
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.created_at}"


STATUS_CHOICES = [
    ('requested', 'Requested'),
    ('pending', 'Pending'),
    ('complete', 'Complete'),
    ('cancelled', 'Cancelled'),
]
class OrderModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    qty = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='requested')

    def __str__(self):
        return f"{self.user.full_name} - {self.status}"
