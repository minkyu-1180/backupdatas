# Vue
## 9. Vue with DRF - 2

## 목차
1. DRF Authentication
2. Authentication with Vue

## 1. DRF Authentication
### Authentication
Authentication : 수신된 요청을 해당 요청의 사용자 또는 자격 증명과 연결하는 메커니즘
- 누구인지를 확인하는 과정(인증)
Permissions : 요청에 대한 접근 허용 또는 거부 여부를 결정(권한)

#### 인증과 권한
1. 인증이 먼저 진행되며, 요청을 해당 요청의 사용자 또는 해당 요청이 서명된 토큰(token)과 같은 일련의 자격 증명과 연결
2. 권한 및 제한 정책(throttling policies)은 인증이 완료된 해당 자격 증명을 사용하여 요청을 허용해야 하는 지를 결정

#### DRF에서의 인증
인증은 항상 DRF에서 view 함수가 시작될 때, 권한 및 제한 확인이 발생하기 전, 다른 코드의 진행이 허용되기 전에 실행됨
- 인증 자체로는 들어오는 요청을 허용하거나 거부할 수 없으며, 단순히 요청에 사용된 자격 증명만 식별
##### 승인되지 않은 응답 및 금지된 응답
1. HTTP 401 Unauthorized : 요청된 리소스에 대한 유효한 인증 자격 증명이 없기 때문에 클라이언트 요청이 완료되지 않았음을 나타냄
2. HTTP 403 Forbidden(Permission Denied) : 서버에 요청이 전달되었지만, 권한 때문에 거절되었음을 나타냄
- 401과 403의 차이점 : 403 같은 경우, 서버는 클라이언트가 누구인지 알고 있음(서버에 요청이 전달이 된 상태)

### 인증 체계 설정
#### 인증 체계 설정 방법
1. 전역 설정 : DEFAULT_AUTHENTICATION_CLASSES를 사용
```python
# settings.py
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
```
2. View 함수 별 설정 : authentication_classes 데코레이터를 사용
```python
# articles/views.py
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
  pass
```
#### DRF 제공 인증 체계
1. BasicAuthentication
2. TokenAuthentication
3. SessionAuthentication
4. RemoteUserAuthentication
#### TokenAuthentication
TokenAuthentication : 간단한 token 기반 HTTP 인증 체계
- 기본 데스크톱 및 모바일 클라이언트와 같은 클라이언트-서버 설정에 적합
- 서버가 사용자들에게 토큰을 발급하여 사용자는 매 요청마다 발급받은 토큰을 요청과 함께 보내 인증 과정을 거침
##### TokenAuthentication 적용 과정
1. 인증 클래스 설정
- TokenAuthentication 활성화 코드 주석 해제
- 기본적으로 모든 view 함수가 토큰 기반 인증이 될 수 있도록 설정
```python
# settings.py
# 1. 인증 클래스 설정(Authentication)
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```
2. INSTALLED_APPS 추가
- INSTALLED_APPS에 rest_framework.authtoken 추가
```python
# settings.py
# 2. INTALLED_APPS에 rest_framework.authtoken 추가
INSTALLED_APPS = [
    .
    .
    'rest_framework',
    # DRF TokenAuthentication 
    'rest_framework.authtoken',
    .
    .
]
```
3. Migrate 진행
- 이유?

4. 토큰 생성 코드 작성
- accoutns/signals.py 생성 후, DRF 문서를 참고하여 코드 작성
- 모든 사용자가 자동으로 생성된 토큰을 가지도록 하는 역할

### DJ-Rest-Auth library
DJ-Rest-Auth : 회원가입, 인증(소셜미디어 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등 다양한 인증 관련 기능을 제공하는 라이브러리
#### DJ-Rest-Auth 설치 및 적용
1. 설치
- pip install dj-rest-auth
2. settings.py의 INSTALLED_APPS에 등록
- 'dj_rest_auth'
3. 프로젝트/urls.py에서 제공하는 urls 사용
- path('accounts/', include('dj_rest_auth.urls')),
#### DJ-Rest-Auth의 등록 기능(registration) 기능 추가 설정
1. 패키지 추가 설치
- pip install 'dj-rest-auth[with_social]'
2. 추가 App 등록
3. 추가 URL 등록
4. Migrate

#### Token 발급 및 활용
##### Token 발급 
1. 회원 가입 및 로그인을 진행하여 토큰 발급 테스트하기
2. 라이브러리 추가로 인해 작성된 URL 목록 확인
- http://127.0.0.1:8000/accounts/ 확인 -> 새로운 7개의 Urls 생성됨(DJ-Rest-Auth 라이브러리의 힘....)
3. 회원가입 진행
- http://127.0.0.1:8000/accounts/signup/
  - Username : test01
  - Password : admin1234!
##### Token 활용

### 권한 정책 설정
#### 권한 설정 방법
1. 전역 설정 : DEFAULT_PERMISSION_CLASSES 사용
```python
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
```
2. View 함수 별 설정 : permission_classes 데코레이더 사용
```python
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
  pass
```

## 2. Authentication with Vue
### 시작 전 확인
- 정상 작동하던 게시글 전체 조회가 작동하지 않음(401 status code)
- 게시글 조회 요청 시 인증에 필요한 수단(token)을 보내지 않고 있으므로, 게시글 조회가 불가능한 상태
