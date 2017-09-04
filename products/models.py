from django.db import models

# Create your models here.

class Categories(models.Model):
    category_id = models.CharField(max_length=20,unique=True,default='C_test',primary_key=True)
    category_name = models.CharField(max_length=200,unique=True,default='test')
    image = models.ImageField(upload_to = 'products/static/products/images/categories',null=True)

    def __str__(self):
        return self.category_name

class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete = models.CASCADE,default=1,related_name='categoryset')
    sub_category_id = models.CharField(max_length=20,unique=True,default='sc_test',primary_key=True)
    sub_category_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200,default='test')

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    product_id = models.CharField(max_length=20,unique=True)
    product_name =models.CharField(max_length=200)
    sub_category = models.ForeignKey(SubCategories, on_delete = models.CASCADE,default=1)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE,default=1)
    product_price = models.IntegerField(default =100)

    def __str__(self):
        return self.product_id

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    pieces_left = models.IntegerField(default = 0)
    pieces_sold = models.IntegerField(default = 0)
    pieces_ordered = models.IntegerField(default = 0)
    total_pieces = models.IntegerField(default = 0)

    def __str__(self):
        return self.total_pieces
