
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'), 
    path('page/', include('pages.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('partners/', include('partners.urls')),
    path('process/', include('processmap.urls')),
    path('library/', views.library, name='library'),
    path('library/files/', include('fileslibrary.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 