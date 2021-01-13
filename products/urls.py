from django.urls import path
from .views import (
    product_update_view,
    product_list_view,
    product_delete_view,
    product_create_view,
    product_detail_view,
    dynamic_lookup_view,
)


app_name = 'products'
urlpatterns = [

    path('productCreate/', product_create_view, name='product-list'),
    path('products/', product_list_view, name='product-list'),
    path('details/',product_detail_view,name='all-products'),
    path('product/<int:my_id>/', dynamic_lookup_view, name='product-details'),
    path('deleteProduct/<int:my_id>/', product_delete_view, name='product-delete'),
    path('updateProduct/<int:my_id>/', product_update_view, name='product-update'),
]