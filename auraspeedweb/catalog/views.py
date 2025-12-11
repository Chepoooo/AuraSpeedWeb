from django.shortcuts import render
from .models import Category, Product
from .models import ContactLink

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
    contact_links = ContactLink.objects.filter(is_active=True).order_by('order')
    
    # Separar por plataforma para el template
    whatsapp_link = contact_links.filter(platform='whatsapp').first()
    instagram_link = contact_links.filter(platform='instagram').first()
    other_links = contact_links.exclude(platform__in=['whatsapp', 'instagram'])
    
    context = {
        'whatsapp_link': whatsapp_link,
        'instagram_link': instagram_link,
        'other_links': other_links,
    }
    return render(request, 'contact.html', context)