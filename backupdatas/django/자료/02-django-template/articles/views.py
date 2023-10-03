import random
from django.shortcuts import render


# Create your views here.
def index(request):
    # dict 형태의 context 변수 생성
    context = {
        'name': 'Jane',
    }
    # render 함수의 3번째 인자로 context를 설정
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = [('국밥', 9000), ('국수', 7500), ('카레', 11000), ('탕수육', 15000),]
    picked = random.choice(foods)
    picked_food = picked[0]
    picked_price = picked[1]
    empty_list = []
    context = {
        'foods': foods,
        'picked': picked,
        'picked_food': picked_food,
        'picked_price': picked_price,
        'empty_list': empty_list,
    }
    # articles라는 디렉토리에 dinner.html로 반환
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # 사용자로 부터 요청을 받아서
    # 요청에서 사용자 입력 데이터를 찾아
    # context에 저장 후 catch 템플릿에 출력
    # print(request)
    # print(type(request))
    # print(request.GET)
    # print(request.META)
    # print(request.GET.get('message'))

    # 요청받은 내용(form 태그에서 입력받은 내용)
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)


def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)
