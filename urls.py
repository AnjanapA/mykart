
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('products_list',views.list_product,name='list_product'),
    path('products_details/<pk>',views.detail_product,name='detail_product'),
]
 