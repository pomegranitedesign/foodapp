from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ItemForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item


class Index(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'


def item(request):
    return HttpResponse('<h1>Hello world</h1>')


class Detail(DetailView):
    model = Item
    template_name = "food/details.html"


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item_form.html', {'form': form})


def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item_form.html', {'form': form, 'item': item})


def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item_delete.html', {'item': item})
