from django.shortcuts import render
from item.models import *
def index(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold= False)
    
    context = {
        
        'items' : items,
        'categories' : categories
               }
    return render(request, 'core/index.html', context=context ) 
def contact(request):
    return render(request, 'core/contact.html')
