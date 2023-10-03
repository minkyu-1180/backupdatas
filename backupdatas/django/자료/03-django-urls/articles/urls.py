from django.urls import path
# 명시적 상대경로
from . import views

# articles 앱의 이름공간 지정
app_name = 'articles'
urlpatterns = [
    # articles 앱에서 생성한 urlpattern별 이름 정의
    # 이후 템플릿에서 url 태그 사용시, {{% url "url이름공간:url이름" %}}으로 사용
    path('', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # path('hello/<str:name>/', views.greeting),
    path('hello/<name>/', views.greeting, name='greeting'),
    path('articles/<int:num>/', views.detail, name='detail'),
]