from unicodedata import name
from django.urls import path
from gold import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name="success"),
]