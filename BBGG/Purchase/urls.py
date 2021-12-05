from django.urls import path

from . import views

app_name = 'Purchase'
urlpatterns = [
    path('<int:ProductID>/', views.index, name='index'),
]