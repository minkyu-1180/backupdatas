from django.shortcuts import render


# Create your views here.
def index(request):
    # render : 페이지를 만들어주는 역할
    # 반드시 request를 가장 첫 인자로 받음
    # 가져와서 응답할 템플릿 경로를 입력
    return render(request, 'articles/index.html')
