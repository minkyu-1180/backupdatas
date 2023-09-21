# pages 앱을 위한 urls
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


app_name = 'pages'
urlpatterns = [
    # url 주소가 길 수도 있으니까... 별명으로 사용
    path('', views.index, name = 'index'),
]