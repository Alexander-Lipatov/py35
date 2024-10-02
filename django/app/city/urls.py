from django.urls import path
from .views import index, news, facts, contacts, managers,city_detail

urlpatterns = [
    path('', view=index, name='index'),
    path('<int:city_id>/', view=city_detail, name='city_detail'),
    path('news', view=news, name='news'),
    path('facts', view=facts, name='facts'),
    path('contacts', view=contacts, name='contacts'),
    path('managers', view=managers, name='managers'),
    
]
    