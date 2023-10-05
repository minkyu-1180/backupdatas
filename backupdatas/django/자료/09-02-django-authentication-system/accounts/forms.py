# accounts/forms.py

# get_user_model() : 현재 프로젝트에서 활성화된 사용자 모델(activae user model)을 반환하는 함수
# get_user_model()을 사용해 User 모델을 참조
# from .models import User
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# UserCreationForm / UserChangeForm : 모두 class Meta: model=User
# -> 커스텀 유저 모델 사용하기 위해 새롭게 작성
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # user model 객체를 리턴해준다
        # 근데 왜 직접 User을 import해서 가져오지 않음???
        # user model에 변경사항이 생길 때 마다 다 바꿔주기 힘들더!
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 회원정보 수정 시, 어떤 field를 공개할 것인가?
        fields = ('first_name', 'last_name', 'email')
        # 비밀번호 전용 변경 폼 존재 : 회원정보 수정과 같이 X
        # 나중에 배울 내용


