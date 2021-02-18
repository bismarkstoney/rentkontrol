
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('contacts/', include('contacts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
