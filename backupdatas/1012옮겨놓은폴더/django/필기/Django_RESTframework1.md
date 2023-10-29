# Django
## Django REST framework 1

## 목차
1. REST API
2. DRF
3. DRF with Single Model

## 1. REST API
### 1-1 .REST API
API(Application Programming Interface) : 애플리케이션과 프로그래밍으로 소통하는 방법
- 클라이언트 <-> 서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계
REST(Representational State Transfer) : API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론 약속(규칙 X)

RESTful API : REST 원리를 따르는 API
- "자원을 정의" & "자원에 대한 주소를 지정"하는 전반적인 방법 서술
- 약속을 만들어서 API 구조 작성 방법을 통일
REST API : REST 설계 디자인 약속을 지켜 구현한 API
#### REST의 약속
REST에서 자원을 정의하고 주소를 지정하는 방법
1. 자원의 식별
- URL
2. 자원의 행위
- HTTP Methods
3. 자원의 표현
- JSON 데이터
- 궁극적으로 표현되는 데이터 결과물
#### 자원의 식별(URL)
URI(Uniform Resource Identifier) : 통합 자원 식별자
- 인터넷에서 리소스(자원)을 식별하는 문자열
URL(Uniform Resource Locator) : 통합 자원 위치
- 웹에서 주어진 리소스의 주소
- Scheme, Domain Name, Port, Path to the file, Parameters, Anchor 순으로 입력됨
ex. 가장 일반적인 URI는 웹 주소로 알려진 URL
#### URL의 구조
1. Schema(or Protocol) : 브라우저가 리소스를 요청하는 데 사용해야 하는 규약
- URL의 첫 부분 : 브라우저가 어떤 규약을 사용하는지를 작성
- 웹 : 기본적으로 HTTP(S)를 요구(메일을 열기 위한 mailto:, 파일 전송을 위한 ftp: 등 다른 프로토콜도 존재)
2. Domain Name : 요청 중인 웹 서버
- 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능(사람이 외우기 어렵게 때문에 주로 Domain Name으로 사용)
ex. 도메인 google.com의 IP 주소는 142.251.42.142
3. Port : 웹 서버의 리소스에 접근하는 데 사용되는 기술적인 문(Gate)
- HTTP 프로토콜의 표준 포트 
    - HTTP : 80
    - HTTPS : 443
- 표준 포트만 생략 가능
4. Path : 웹 서버의 리소스 경로
- 초기 : 실제 파일이 위치한 물리적 위치
- 요즘 : 실제 위치가 아닌, 추상화된 형태의 구조를 표현
ex. /articles/creaet/ : 실제 articles 폴더 안에 create 폴더 안을 나타내는 것 X
5. Parameters : 웹 서버에 제공하는 추가적인 데이터
- '&' 기호로 구분되는 key-value 쌍 목록
- 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행 가능
6. Anchor : 일종의 북마크 역할(브라우저의 해당 지점에 있는 콘텐츠 표시)
- fragment identifier(부분 식별자)라고 부르는 '#' 이후 부분은 서버에 전송 X

#### 자원의 행위(HTTP Request Methods) 
HTTP Request Methods : 리소스에 대한 행위(수행하고자 하는 동작)를 정의
- called HTTP verbs
#### 대표적인 HTTP Request Methods
1. GET
- 서버에 리소스의 표현 요청
- GET을 사용하는 요청은 only 데이터 검색
2. POST
- 데이터를 지정된 리소스에 제출
- 서버의 상태를 변경
3. PUT 
- 요청한 주소의 리소스를 수정
4. DELETE
- 지정된 리소스 삭제
#### HTTP response status codes
HTTP response status codes : 특정 HTTP 요청이 성공적으로 완료 되었는지에 대한 여부
- Informational response : 100 ~ 199
- Successful response : 200 ~ 299
- Redirection messages : 300 ~ 399
- Client error responses : 400 ~ 499
- Server error responses : 500 ~ 599

#### 자원의 표현(JSON type)
서버의 응답
- 기존 Django 서버는 사용자에게 페이지(html)만을 응답
- 서버가 응답할 수 있는 것 : 다양한 데이터 타입 
- RESP API 권장사항 : JSON 타입으로 응답
- Django는 더이상 Temlate 부분에 대한 역할 담당 X(Front-end와 Back-end가 분리되어 구성)
- 우리가 할 것 : Django를 이용하여 REST API Server 구축

#### 사전 준비
- 99-json-response-practice 기반 시작

1. 가상환경 생성, 활성화 및 패키지 설치
2. migrate 진행
3. 준비된 fixtures 파일을 load하여 실습용 초기 데이터 입력
- python manage.py loaddata articles.json

+ python으로 json 응답 받기
## 2. DRF
### DRF
DRF(Django REST framework) : Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
#### Serialization
Serialization : 직렬화, 포장
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정
## 3. DRF with Single Model
### 프로젝트 준비
- 사전 제공된 drf 프로젝트 기반 시작
- 가상 환경 생성, 활성화 및 패키지 설치
- migration 진행
- 준비된 fixtures 파일을 load 하여 실습용 초기 데이터 입력
- Postman(API 구축을 위한 플랫폼) 설치

### URL & HTTP requests methods 설계
### 1. GET
#### GET - articles 조회
1. 게시글 데이터 목록을 제공하는 ArticleListSerializer 정의
2. url 및 view 함수 작성
```python
# articles/serializers.py
from rest_framework import serializers
from .models import Article

# ModelSerializer 생성(Django 모델과 연결된 Serializer 클래스)
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
# artlcles/urls.py
urlpatterns = [
    path('ariticles/', views.article_list)
# articles/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleLiseSerializer

# GET 메서드만 허용되며, 다른 메서드 요청에 대해서는 '405 Method Not Allowed'로 응답
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    # JSON 데이터 여러 개 -> many=True 설정
    serializer = ArticleLiseSerialzer(articles, many=True)
    # JSON 데이터로 serialization -> html 페이지 없이 응답하는 현재의 view 함수
    return Response(serializer.data)
]
```
#### GET - Detail 조회
1. 각 게시글의 상세 정보를 제공하는 ArticleSerializer 정의
2. url 및 view 함수 작성
```python
# articles/serializers.py
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

# ariticles/urls.py
urlpatterns = [
    path('articles/<int:article_pk>/', views.article_detail),
# articles/views.py
from .serializers import ArticleSerializer

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
]
```

### POST - 데이터 생성
#### article_list view함수 구조 변경(GET or POST)
```python
# articles/views.py
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    # GET -> 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # POST -> 생성
    elif request.method == 'POST': 
        # 단일 게시글 생성(request.data를 데이터로 사용)
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            # 유효성 검사 성공 시, serializer의 데이터와 HTTP 응답 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사 실패 시, serializer의 에러값과 HTTP 응답 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### DELETE
단일 게시글 데이터에 대해 조회 or 삭제
- view 함수의 article_detail 수정
```python
# articles/views.py
@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### PUT
단일 게시글 데이터 수정 
- view 함수의 article_detail 수정
```python
# article/views.py
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 수정은 생성과 비슷
    elif request.method == 'PUT':
        # 수정 : instance 인자값 필요
        serializer = ArticleSerializer(instance=article, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
#### 정리
1. article_list : GET & POST
- GET : 전체 게시글 조회(serializer = ArticleSerializer(articles, many=True))
- POST : 단일 게시글 생성(serializer = ArticleSerializer(data=request.data))
2. article_detail : GET, DELETE, PUT
- GET : 단일 게시글 조회(serializer = ArticleSerializer(article))
- DELETE : 단일 게시글 삭제(article.delete())
- PUT : 단일 게시글 수정(serializer = ArticleSerializer(instance=article, data=request,data))

#### 참고
raise_exception : is_valid() 유효성 검사에서 사용하는 인자
- ValidationError 예외를 발생시키는 선택적 인자
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며, 기본적으로 HTTP 400 응답 반환
```python
if serializer.is_valid(raise_exception=True):
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
