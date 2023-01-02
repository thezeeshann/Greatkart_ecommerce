from .models import Category

# fetch all the category in the database
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)