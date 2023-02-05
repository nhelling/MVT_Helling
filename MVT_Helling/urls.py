from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from MVT_Helling.settings import MEDIA_ROOT, MEDIA_URL
from MVT_Helling.views import inicio, index,about_us


urlpatterns = [
    path('',index, name = 'index'),
    path('admin/', admin.site.urls),
    path('Inicio/',inicio),
    
    path('about_us/',about_us),      
    path('fleet/', include ('fleet.url')),
    path('flights/', include('flights.url')),
    path('routes/', include('routes.url')),
    path('users/', include('users.url')),
    path('initial/', include ('initial.url')),
    
    
    
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
