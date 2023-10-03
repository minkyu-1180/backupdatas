from django.db import models

# Create your models here.

# 게시글이 작성되는 테이블 생성
class Article(models.Model): # models라는 모듈의 Model 클래스 상속
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
