from django.contrib import admin
from .views import *
from django.urls import path

from . import views

pp_name='app'

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',blog, name='blog'),
    path('blog/<int:pk>',posting, name="posting"),
]