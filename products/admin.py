from django.contrib import admin
from .models import Product, Stock, Categories, SubCategories
# Register your models here.
admin.site.register(SubCategories)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Stock)
