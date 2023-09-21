from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 함수 내에 dict 작성
    context = {
        'name' : 'Jane',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }

    return render(request, 'articles/dinner.html', context)

def search(request):

    return render(request, 'articles/search.html')

def throw(request):
    
    return render(request, "articles/throw.html")

def catch(request):
    print(request)
    print(type(request))
    # request의 key값인 GET
    # GET에 저장된 내용 : key-value로 이루어진 query-dict 
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    # thrwo에서 요청을 받아서
    # 요청(request) 내에서 사용자 입력 데이터를 찾아
    # context에 지정 후 catch 템플릿에 출력
    
    return render(request, "articles/catch.html", context)

# view함수에 새로운 파라미터가 필요한 경우
def greeting(request, name):
    context = {
        'name' : name,
    }
    return render(request, "articles/greeting.html", context)


def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, "articles/detail.html", context)