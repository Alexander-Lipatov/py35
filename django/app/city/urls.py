from django.urls import path
from .views import index, news, facts, contacts, managers

urlpatterns = [
    path('', view=index, name='index'),
    path('news', view=news, name='news'),
    path('facts', view=facts, name='facts'),
    path('contacts', view=contacts, name='contacts'),
    path('managers', view=managers, name='managers'),
]
    