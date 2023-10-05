# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
# forms.py에서 제작한 Custom User Form 활용
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("articles:index")
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # 기존 : 로그인을 할 경우, 반드시 index로 갔음...
            # next parameter가 존재하는 상태로 올 경우, next가 우선순위
            # 1. 첫 번째 방법
            # if request.GET.get('next'): next가 GET 요청에 있다면
            #   return redirect(request.GET.get('next'))
            # return redirect('articles:index')
            # 2번째 방법
            # 만약 너가 create, delete같이 로그인이 된 상태에서 해야 하는 것을
            # 로그인이 안된 상태로 해서 login_required에 걸려서 next의 값이 생긴 거라면
            # 그 때, 로그인에 성공하게 된다면 next에 저장된 주소로 가!
            # 그게 아니라, 너가 정상적으로 로그인 버튼을 눌러서 이 함수가 호출된 것이면
            # 로그인에 성공하게 될 경우, articles/index/로 가!
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect("articles:index")
    if request.method == 'POST':
        #
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() # 회원가입 -> DB에 저장
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # 요청하는 유저 객체 삭제
    request.user.delete()
    auth_logout(request)
    return redirect("articles:index")

@login_required
def update(request):
    if request.method == 'POST':
        # 수정 : 기존 객체도 인자로 받음(생성과 수정 구분을 위해)
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
# /user_pk/password url -> 비밀번호 변경 함수 호출
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # 새롭게 갱신하여 DB에 저장된 값을 user에 저장 -> 세션 갱신 가능
            user = form.save()
            update_session_auth_hash(request, user) # 새롭게 갱신된 유저 정보를 인자로 
            # 비밀번호가 변경된 후, 로그아웃되버림 와이??
            # 비밀번호 변경 : 인증된 사용자의 Session 데이터를 Update하는 과정 -> 브라우저 입장에서 Session id의 key가 안맞음(세션이 무효화)
            # update_session_auth_hash(request, user) : 암호 변경 시 세션 무효화를 막아주는 함수
            # 새로운 password의 세션 id로 기존 세션 갱신
            return redirect("articles:index")
    else:
        # 유저 객체 : 필수 위치 인자(SetPasswordForm : PasswordChangeForm의 부모 폼)
        # 기존 폼들과 다르게 인자의 구성 요소가 다르네요...
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)