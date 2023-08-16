from django.urls import path
from .views import product_list
from django.conf.urls.static import static
from config.settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('', product_list, name='product-list'),
]

