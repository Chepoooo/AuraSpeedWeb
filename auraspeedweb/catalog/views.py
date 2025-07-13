from django.shortcuts import render
from .models import Category, Product

def catalog(request):
    categories = Category.objects.all()
    products_by_category = {}
    
    for category in categories:
        products_by_category[category] = Product.objects.filter(category=category)
    
    context = {
        'categories': categories,
        'products_by_category': products_by_category
    }
    return render(request, 'catalog.html', context)
  
def contact(request):
  return render(request,'contact.html')