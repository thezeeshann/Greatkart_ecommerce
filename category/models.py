from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True,max_length=100)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to="photos/category",blank=True)

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
    