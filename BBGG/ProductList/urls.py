from django.urls import path

from . import views

app_name = 'ProductList'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ProductID>/', views.detail, name='detail'),
]
