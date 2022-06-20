from .views import *
from django.urls import path

from . import views

pp_name='app'

urlpatterns=[
    path('',index),
]