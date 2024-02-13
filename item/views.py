from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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

@login_required
def edit(request, pk):
    item = get_object_or_404(Item , pk=pk , created_by = request.user)
    if request.method == 'POST':
        

        form = EditItemForm(request.POST, request.FILES, instance= item)
        if form.is_valid:
            form.save()

            return redirect('detail', pk = item.id)
    else:
        form = EditItemForm(instance= item)


    context = {
        'form' : form,
        'title' : 'Edit item'
    }

    return render(request, 'item/form.html' , context)


def items(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    if query:
        items = items.filter(Q(name__icontains= query) | Q(description__icontains= query))

    if category_id :
        items = items.filter(Category_id = category_id)
    context = {
        'items' : items,
        'query' : query,
        'categories' : categories,
        'category_id' : int(category_id),
    }
    return render(request, 'item/browser.html', context)