from django.contrib import admin
from .models import  *
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(VendorModel)
admin.site.register(OrderModel)