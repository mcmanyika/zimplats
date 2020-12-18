from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from libs.views import *

urlpatterns = [

url(r'^success/', success, name='success'),
url(r'^logout/$', Logout, name='logout'),
url(r'', form, name='form'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
