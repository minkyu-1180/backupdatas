from django.urls import path
from articles import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list), # 댓글 목록 조회
    path('comments/<int:comment_pk>/', views.comment_detail), # 단일 댓글 조회
    path('articles/<int:article_pk>/comments/', views.comment_create),

    
]

