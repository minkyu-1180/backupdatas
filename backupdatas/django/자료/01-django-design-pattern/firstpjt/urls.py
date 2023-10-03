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
# articles라는 패키지의 views 모듈을 불러오기
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # https://127.0.0.1:8000/articles로 요청이 올 떄, views 모듈의 index 뷰 함수를 호출
    path('articles/', views.index),
]
