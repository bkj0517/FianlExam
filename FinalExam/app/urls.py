from django.contrib import admin
from .views import *
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from . import views

pp_name='app'

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',blog, name='blog'),
]

