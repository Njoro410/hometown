from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Index, name='index'),
    path('home/',views.Home,name='home'),
    path('addpost/',views.Create_posts,name='addpost'),
    path('addbusiness/',views.AddBusiness,name='addbusiness'),
    path('business/<str:id>/',views.Businesses,name='business'),
    path('hospital/<str:id>/',views.Hospital,name='hospital'),
    path('police/<str:id>/',views.Law,name='police'),
    path('userprofile/<str:id>/',views.UserInfo,name='userinfo'),
    path('admin/',views.admin,name = 'panel')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)