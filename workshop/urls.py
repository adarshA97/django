from django.conf.urls import include,url
from django.contrib import admin
from registration.views import Home
from registration import urls as reg_urls


urlpatterns = [
     url(r'^$', Home.as_view(), name='home'),
     url(r'^workshop/', include(reg_urls)),
     url(r'^registration/', include(admin.site.urls)),
]