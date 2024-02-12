from django.shortcuts import render, redirect
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

    if request.method== 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()



    
    context = {
        'form' : form,
    }
    return render(request , 'core/signup.html', context)
