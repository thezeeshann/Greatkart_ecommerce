from django.urls import path
from . import views

urlpatterns = [
    path('place_order/',views.PlaceOrder,name='place_order'),
    path('paymensts/',views.Payments,name='payments'),
    path('order_complete/',views.order_complete,name='order_complete')
]
