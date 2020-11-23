from .forms import ItemForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item


def index(request):
    items = Item.objects.all().order_by('-created_at')
    context = {'items': items}
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse('<h1>Hello world</h1>')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'food/details.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item_form.html', { 'form': form })
    

def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item_form.html', { 'form': form, 'item': item })

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item_delete.html', { 'item': item })