from django.urls import path
from app2.views import *
app_name='everything'
urlpatterns=[
    path('giri2/',giri2,name='giri2'),
    ]