from users import views as user_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', name="register", view=user_views.register)
]
