from django.contrib import admin
from .models import Product,Variation,ReviewRating,ProductGallery
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','is_available','created_date','modified_date','image','category')
    prepopulated_fields = {"slug":("product_name",)}
    inlines = [ProductGalleryInline]
admin.site.register(Product,ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variaton_category','variaton_value','is_active','created_date')
    list_editable = ('is_active',)
    list_filter = ('product','variaton_category','variaton_value')
admin.site.register(Variation)


class ReviewRatingAdmin(admin.ModelAdmin):
    pass
admin.site.register(ReviewRating,ReviewRatingAdmin)