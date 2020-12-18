
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    url(r'^', include('libs.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
