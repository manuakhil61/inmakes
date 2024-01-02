from . import views
from django.urls import path

import travelapp

urlpatterns = [
    path('',views.demo,name='demo')
]
