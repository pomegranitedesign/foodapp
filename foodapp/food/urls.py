from django.urls import path
from .views import Detail, edit_item, Index, item, create_item, delete_item

app_name = 'food'
urlpatterns = [
    path('', name='index', view=Index.as_view()),
    path('item/', name='item', view=item),
    path('<int:pk>/', name='item_details', view=Detail.as_view()),
    path('add', name="create_item", view=create_item),
    path('edit/<int:item_id>', name="edit_item", view=edit_item),
    path('delete/<int:item_id>', name="delete_item", view=delete_item)
]
