from users import views as user_views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout, views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', name="register", view=user_views.register),
    path('login/', name="login",
         view=auth_view.LoginView.as_view(template_name='users/login.html')),
    path('logout/', name='logout',
         view=auth_view.LogoutView.as_view(template_name='users/logout.html')),
    path('profile/', name='profile', view=user_views.profile)
]

urlpatterns += [
    # Some other urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
