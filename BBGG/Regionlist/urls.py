from django.urls import path

from . import views

app_name = 'Regionlist'
urlpatterns = [
    path('', views.index, name='index'),
]