from django.urls import path
from . import views

urlpatterns = [
    path('',views.Carts,name='cart'),
    path('add_cart/<int:product_id>/',views.AddCart,name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/',views.RemoveCart,name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/',views.RemoveCartItem,name='remove_cart_item'),
    path('checkout/',views.CheckOut,name='checkout')
]