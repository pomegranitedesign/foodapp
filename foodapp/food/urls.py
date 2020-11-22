from django.urls import path
from .views import index, item

urlpatterns = [
    path('', name='index', view=index),
    path('item/', name='item', view=item)
]
