from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def detail(request, pk):
    
    item = get_object_or_404(Item, pk=pk)
    retlated_items = Item.objects.filter(Category = item.Category, is_sold = False).exclude(pk = pk)[0:6]
    
    context = {
        'items' : item,
        'related_items' : retlated_items
    }
    return render(request, 'item/detail.html', context=context)

@login_required
def new(request):
    if request.method == 'POST':

        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid:

            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('detail', pk = item.id)
    else:
        form = NewItemForm()


    context = {
        'form' : form,
        'title' : 'New item'
    }

    return render(request, 'item/form.html' , context)

@login_required
def delete(request, pk):
    item = get_object_or_404(Item , pk=pk , created_by = request.user)
    item.delete()
    return redirect('index')
