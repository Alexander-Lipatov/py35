from django.contrib import admin
from django.urls import path, re_path
from .views import index


urlpatterns = [
    path('1/1/', view=index, name='index'),
    re_path(r'^(?P<slug>\d+)?/$', index ,name = 'index'),
]
