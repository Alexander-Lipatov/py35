from django.contrib import admin
from django.urls import path, re_path
from .views import index, table_mult, dev_day


urlpatterns = [
    path('', view=index, name='index'),
    path('table_mult/', view=table_mult, name='table_mult'),
    path('dev_day/', view=dev_day, name='dev_day'),
    # re_path(r'^(?P<slug>\d+)?/$', index ,name = 'index'),
]
