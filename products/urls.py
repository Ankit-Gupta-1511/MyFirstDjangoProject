from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_name>[A-Z]+\w\D$)',views.sub_categories,name='sub_categories'),
    url(r'^product-list', views.products, name='products'),
    url(r'^(?P<product_id>P_[0-9]+\w$)',views.detail,name='product_detail'),
]
