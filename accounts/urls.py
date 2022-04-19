from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register, name ='register' ),
    path('login/',auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'index.html'), name='logout'),
    path('profile/',views.user_info,name='profile'),
    # path('hood/',views.area,name='hood')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)