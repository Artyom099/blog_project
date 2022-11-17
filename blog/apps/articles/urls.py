from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),      # вызываем views.index
    path('test/', views.test, name = 'test'),   # вызываем views.test
]
