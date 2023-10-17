from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 내가 상대방을 팔로우를 건다
    # 맞팔 방지를 위해 대칭(1이 2를 팔로우할 경우, 자동으로 2가 1을 팔로우하는 것 방지) False
    # 역참조 시, related manager name을followers로 바꾸기
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
