from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Store,name='store'),
    path('<slug:category_slug>/',views.Store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.ProductDetail,name='products_details'),
    path('submit_review/<int:product_id>/',views.submit_review,name='submit_review')
]
