from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # url이 /articles/까지 -> index 함수(html에서 articles:index)
    path('', views.index, name='index'),
    # url이 /articles
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
