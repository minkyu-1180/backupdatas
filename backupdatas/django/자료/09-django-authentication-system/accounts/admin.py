from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

# 관리자 사이트에 우리가 정의한 User model을 볼 수 있도록 등록
admin.site.register(User, UserAdmin)