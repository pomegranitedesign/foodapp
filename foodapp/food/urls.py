from django.urls import path
from .views import detail, edit_item, index, item, create_item, delete_item

app_name = 'food'
urlpatterns = [
    path('', name='index', view=index),
    path('item/', name='item', view=item),
    path('<int:item_id>/', name='item_details', view=detail),
    path('add', name="create_item", view=create_item),
    path('edit/<int:item_id>', name="edit_item", view=edit_item),
    path('delete/<int:item_id>', name="delete_item", view=delete_item)
]
