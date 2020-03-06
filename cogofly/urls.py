from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

admin.site.site_title = "Administration Cogofly" 
admin.site.site_header = "Administration Cogofly" 

urlpatterns = [
    
    path("", include("home.urls")),
    path("accounts/", include('allauth.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
