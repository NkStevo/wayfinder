from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^wayfinder/', include('wayfinder_app.urls')),
    url(r'^admin/', admin.site.urls),
]
