from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login # 로그인 세션 데이터 생성 모듈(별명 이유 : def login과 이름이 겹침)
from django.contrib.auth import logout as auth_logout
# Create your views here.
def login(request):
    # 로그인 시도
    if request.method == 'POST':
        # session create
        # AuthenticationForm : forms를 상속 -> 첫 번째 인자로 request, 두 번째 인자를 request.POST 를 받음
        form = AuthenticationForm(request, request.POST)
        # 유효성 검사
        if form.is_valid():
            # 유효성 검사 통과시, 로그인(세션 데이터 생성)
            # request, 유저 데이터를 인자로 받아서 사용
            auth_login(request, form.get_user())
            # 메인 페이지로 redirect
            # 만약 로그인에 성공한 경우, redirect된 페이지에서 개발자 도구 -> Application -> Cookie 확인시 가능(sessionid)
            # 실제 세션 데이터는 db.sqlite3 -> django_session에 보관(알아서 다 해주네!)
            return redirect("articles:index")
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    # 로그아웃에 성공한 경우, redirect된 페이지에서 개발자 도구 -> Application -> Cookie 확인시, session id가 삭제됨
    # db.sqlite3 -> django_session에서도 사라짐
    return redirect("articles:index")