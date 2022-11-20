from . import views
from django.urls import path

app_name = 'articles'       # указываем, из какого приложения барть ссылки
urlpatterns = [
    path('', views.index, name = 'index'),      # вызываем views.index
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
