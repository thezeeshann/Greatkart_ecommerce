from django.shortcuts import render
from store .models import Product
from store.models import ReviewRating

def Home(request):
    # try:
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    # Get the reviews
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    # except Exception as e:
    #     print(e)
    context = {
        'products':products,
        'reviews':reviews
    }
    return render(request,'index.html',context)