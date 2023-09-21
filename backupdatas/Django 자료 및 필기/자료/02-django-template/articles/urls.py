# articles 앱의 전용 url
"""
URL configuration for firstpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 명시적 상대경로
from . import views # 현재 디렉토리(articles 앱의 하위)에서 views 모듈 가져오기 

# 태그 붙여주기
app_name = 'articles'
urlpatterns = [
    # url 주소가 길 수도 있으니까... 별명으로 사용
    path('', views.index, name='index'), # 받은 주소와 이름이 같을 경우(기존이 'articles/'였음)
    path('dinner/', views.dinner, name = 'dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # <type:변수명>
    path('hello/<str:name>/', views.greeting),
    path('articles/<int:num>/', views.detail),
]
