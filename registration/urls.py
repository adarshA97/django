from django.conf.urls import include, url
from django.contrib import admin
from registration.views import *

urlpatterns = [
url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    ]