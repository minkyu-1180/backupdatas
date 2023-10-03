from django.contrib import admin
from .models import Article

# 관리자 페이지에서 Article이 뜨길 원할 경우 : 등록
admin.site.register(Article)
