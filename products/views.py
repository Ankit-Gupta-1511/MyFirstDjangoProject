from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Stock, Categories, SubCategories
# Create your views here.
all_categories = Categories.objects.all()
sub_categories_menu = SubCategories.objects.all()
def index(request):
    all_categories = Categories.objects.all()
    template = loader.get_template('products/index.html')
    context = {
        'all_categories': all_categories,
        'sub_categories_menu': sub_categories_menu,
    }
    return HttpResponse(template.render(context, request))

def sub_categories(request, category_name):
    current_category = Categories.objects.get(category_name = category_name)
    data = current_category.categoryset.all()
    template = loader.get_template('products/sub_categories.html')
    context = {
        'all_categories': all_categories,
        'sub_categories_menu': sub_categories_menu,
        'all_sub_categories': data,
    }
    return HttpResponse(template.render(context, request))


def products(request):
    all_products = Product.objects.order_by('id')
    template = loader.get_template('products/product-list.html')
    context = {
        'all_categories': all_categories,
        'sub_categories_menu': sub_categories_menu,
        'all_products': all_products,
    }
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    all_products = Product.objects.all()
    template = loader.get_template('products/product-detail.html')
    for product in all_products:
        if(product.product_id == product_id):
            context = {
                'all_categories': all_categories,
                'sub_categories_menu': sub_categories_menu,
                'product': product,
            }
            return HttpResponse(template.render(context, request))
