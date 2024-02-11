from django.shortcuts import render
from item.models import *
from .forms import SignUpForm
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

def signUp(request):
    form = SignUpForm()
    context = {
        'form' : form,
    }
    return render(request , 'core/signup.html', context)
