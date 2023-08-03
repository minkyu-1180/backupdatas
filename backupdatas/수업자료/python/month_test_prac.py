# 1. Fundamentals of Python

# 연산자 순위
# () -> [] -> ** -> +,-(부호) -> *,/,//,% -> +,-
# -> 비교 -> 객체비교(is, is not) -> 멤버십(in, not in)
# -> 논리 부정(not) -> and -> or
print(-2 ** 4) # ** -> -(부호) : -16
print(-(2 ** 4)) # () -> ** -> -(부호) : -16
print((-2) ** 4) # () -> ** : 16

# 변수의 재할당
# 변수 number에 int형 객체 10 할당
number = 10 
# 변수 double에 number * 2 할당 : 새로운 메모리 주소에 객체 할당하여 참조
double = number * 2 
print(double) # 20
number = 5
# double은 number에 재할당을 하는 것과 상관없이 이미 새로운 주소에
# int형 20을 객체로 하여 참조
print(double) # 20
print()

# 2. Data Types

# int 자료형
# 진수 -> 10진법
print(0b11) # 2진수 11을 10진법으로 표현 : 1 * 2 + 1 * 1 = 3
print(0o27) # 8진수 27을 10진법으로 표현 : 2 * 8 + 7 * 1 = 23
print(0x1A2) # 16진수 1A2를 10진법으로 표현 # 1 * 256 + 10 * 16 + 12 * 1 = 428

# float 자료형
# floating point rounding error 방지
a = 3.2 - 3.1
b = 1.2 - 1.1

print(abs(a - b) <= 1e-10)
import math
print(math.isclose(a, b))

# Seq

# str
# 순서 O / 반복 O / 중복 O / 수정 X
str1 = 'Hello, World!'
str2 = 'My Phone number is 010-2742-1655'

print(str1)
for x in str2:
    # string 안의 요소는 모두 str type이다!
    # 그것이 겉으로 보기에는 숫자더라도,,,
    print(x, type(x))

# 중첩따옴표
print("My name is 'MK Kim'!")
print('What\'s your name?')

print('This is\tTab')
print('This is\nEnter')
# f-string
name = 'Minkyu'
print(f'Hello! My name is {name}.\nNice to meet you!')

# 문자열은 불변이다.
my_str = 'Good morning'
# my_str[0] = T같이 문자열의 요소는 수정 불가능!!!

# 문자열은 수정을 못하기 때문에, 새로운 빈 문자열을 만들고 넣어주는 방식
my_new_str = ''
for x in my_str:
    if x == 'G':
        x = 'T'
    my_new_str += x
print(my_new_str)
print()

# list
# 리스트의 요소는 가변
# str처럼 한 메모리 주소에 문자열이 통째로 들어가는게 아님
# 요소 수정을 할 경우, 그냥 참조 방향만 바꿔주면 되기 때문

# 중첩 리스트
my_list = [1, 2, 3, ['Hello', 'Python']]
print(my_list[-1][0])

# tuple
# 순서 O / 반복 O / 중복 O / 수정 X
tuple1 = () # 빈 튜플
tuple2 = (1, ) # 요소의 개수가 한 개인 튜플 표기법
tuple3 = 1, 2, 3, 4 # 여러 개의 요소가 있을 경우 괄호 생략 가능
print(tuple1)
print(tuple2)
print(tuple3)
print()
# range : 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
# 순서 O / 반복 O / 중복 X / 수정 X
my_range1 = range(10) # 0 ~ 9
my_range2 = range(1, 5) # 1 ~ 4

# 역순으로 정수 시퀀스를 생성하고 싶을 경우!!!!
my_range3 = range(10, 7, -1) # 10, 9, 8
print(list(my_range1))
print(list(my_range2))
print(list(my_range3))
print()

# Non-seq

# dictionary
# 순서 X / 반복 O / 중복 X(키중복 X) / 수정 O
# 키에 들어갈 수 있는 자료형 : 변경 불가능한 자료형
# int, str, tuple 
my_dict1 = {} # 빈 딕셔너리 생성
my_dict2 = {'name' : 'Kim'}
my_dict3 = {'name' : 'Lee',
            'age' : 16,
            'address' : 'Seoul',
            'job' : 'student'}
# value 출력 : 해당 value의 키로 접근
print(my_dict3['name'])
# 새로운 키 - 값 쌍 추가
my_dict3['ismarried'] = True
# 키에 할당된 값 수정
my_dict3['age'] = 23
print()
# set
# 순서 X / 반복 O / 중복 X / 수정 O
# 빈 세트 생성 방법 : {}로 하면 빈 딕셔너리가 되게 때문에 set()함수 사용
my_set1 = set()
# 세트는 중복 허용 X : 알아서 지워줌
my_set2 = {1, 2, 3, 3, 4, 5, 6}

# 세트 연산
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6, 7, 8}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)

# Other Types

# None 
var_1 = None 
print(None)
print(bool(None)) # False
print()
# Boolean
bool1 = True
bool2 = False
print(bool1)
print(bool2)
print(1 > 3)
print('2' != 2)

# Collection 
# str, list, tuple, dict, set

# 3. Type Conversion

# Implicit TC
print(3 + 5.0)
print(True + 3 * False)
print()
# Explicit TC
print(int(3.14))
print(str(1.2345))
print()
# print(int('3.14'))는 오류가 발생함
# print(int('안녕하세요'))도 오류가 발생함

# 4. Operator

# 산술 연산자 & 복합 연산자

# 비교 연산자
# >, >=, <, <=, ==, != : equality
# is 비교 연산자 : identity

# 논리 연산자(and, or, not)
# 단축평가
my_str_1 = 'HelloWorld!?!'

print(('b' and 'd') in my_str_1)
# 'b' : True --and--> 'd' : True 
# -> 뒤의 True인 'd'가 해당 논리 연산자의 결과 
# 문제 : 'd' in my_str_1 : True
print(('d' and 'b') in my_str_1)
# 'b' : True --and--> 'b' : True 
# -> 뒤의 True인 'b'가 해당 논리 연산자의 결과 
# 문제 : 'b' in my_str_1 : False
print()

# 멤버십 연산자

word = 'ByeBye Friends'
print('h' in  word) 
print('y' in word)
print()
# 시퀀스형 연산자
# 기존의 산술 연산자 +, *와 다른 역할
print('KIM' + 'Minkyu') # KimMinkyu
print('Hello' * 3) # HelloHelloHello
print()

# 5. Functions

'''
# 함수 정의
def func_name(pos1, pos2, default_arg = 'default', *args, **kawrgs):
    # Docstring
    function body
    return return_value

# 함수 호출
print(func_name(args))
'''

# global 키워드
global_var = ['Hello', 'Python', '3-11!']

def my_func():
    # 글로벌 선언(수정 전에 선언할 것)
    # 글로벌 선언할 값은 매개변수로 지정 불가
    global global_var
    global_var[2] = '3-9'
    return global_var

print(my_func())
print()

# 재귀함수
# 종료 조건(base case)에 수렴하도록 함수 짜기
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print()

# map(func, iter)
my_iter_list = [1, 3, 5, 7, 9, 11, 13, 15]
add_self = lambda x : x * 2 
print(list(map(add_self, my_iter_list)))
print()

# zip(*iters)
fruit_price = {'apple' : 1500,
               'banana' : 3000, 
               'lemon' : 4500,
               'melon' : 12000}

fruit_num = {'apple' : 3,
             'banana' : 5,
             'lemon' : 12,
             'melon' : 2}
print(list(zip(fruit_price.values(), fruit_num.values())))


# lambda
# lambda 매개변수(여러개 가능, ,로 구분) : 표현식

# 6. Packing & Unpacking

# packing
packed = 1, 2, 3, 4 ,5
print(packed) # 튜플 형태로 묶어서 할당
print()
my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, b, c,*d, e = my_lst # *를 사용하여 남은 요소들을 리스트로 패킹
print(a, b, c)
print(d)
print(e)
print()
# unpacking
v1, v2, v3, v4, v5 = packed # 묶여져 있는 변수의 값을 개별 요소로 분리하여 할당
print(v1, v2, v3, v4, v5)

greeting_list = ['Hi', 'Hello', 'Goodmorning', 'Nice to see you']
print(*greeting_list) # 기존에 묶여있던 값들을 언패킹

def unpacking_func(x, y, z):
    # return으로 하니까 튜플형태로 묶여서 반환됨
    print(x, y, z)

my_dict = {'x' : 1, 'y' : 2, 'z' : 3}
unpacking_func(**my_dict)
print()

# 7. Module

# 8. Control of Flow

# if statement

# if-elif-else
a = 5
if a > 3:
    print('3 초과')
elif a < 3:
    print('3 미만')
else:
    print('a는 3이 맞습니다.')
print()

# if-elif-else
dust = int(input("오늘의 미세먼지 농도를 입력하시오. : "))

if dust > 150:
    print('오늘의 미세먼지 농도는 매우 나쁩니다.')
elif dust > 80:
    print('오늘의 미세먼지 농도는 나쁩니다.')
elif dust > 50:
    print('오늘의 미세먼지 농도는 보통입니다.')
else:
    print('오늘의 미세먼지 농도는 낮습니다.')

# 중첩 조건문
dust = int(input("오늘의 미세먼지 농도를 입력하시오. : "))

if dust > 150:
    print('오늘의 미세먼지 농도는 매우 나쁩니다.')
    if dust > 300:
        print('너무 나쁜 편이니 외출을 자제하시기 바랍니다.')
elif dust > 80:
    print('오늘의 미세먼지 농도는 나쁩니다.')
elif dust > 50:
    print('오늘의 미세먼지 농도는 보통입니다.')
else:
    print('오늘의 미세먼지 농도는 낮습니다.')

# 반복문

# for
# iterable 데이터 구조의 요소에 순차적으로 접근하여 반복해서 코드 실행
# list, dict, set, str, bytes, tuple, range
items = ['apple', 'banana', 'coconut']

# for문 : item에 iterable 데이터 items의 요소들을 순차적으로 할당
for item in items:
    print(item)
print()

# 중첩 반복문
for i in range(1, 10):
    print(f'{i}단을 외자!')
    for j in range(1, 10):
        print(f'{i} X {j} = {i * j}')
    print()    
        
# while
# 주어진 조건식이 False가 될 때 까지 반복해서 코드 실행
count = 1
my_num = int(input('당신의 값을 입력하시오.'))
answer = 7
while count < 5:
    if my_num == answer:
        print(f'당신은 {count}번 만에 정답을 찾았습니다.')
        print(f'정답은 {answer}입니다.')
        break
    elif my_num > answer:
        count += 1
        print(f'정답은 당신의 값 {my_num}보다 작습니다.')
        my_num = int(input('값을 재입력하시오.'))
    else:
        count += 1
        print(f'정답은 당신의 값 {my_num}보다 큽니다.')
        my_num = int(input('값을 재입력하시오.'))
else:
    print(f'당신은 {count}번만에 맞추기를 실패했습니다.')
    print(f'정답은 {answer}입니다.')
    print('프로그램을 종료합니다.')
    
