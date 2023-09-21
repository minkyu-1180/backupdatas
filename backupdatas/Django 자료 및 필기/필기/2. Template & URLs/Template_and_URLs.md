# 2. Template and URLs

## 목차
1. Django Template
- Template System
- 템플릿 상속
- HTML form(요청과 응답)
2. Django URLs
- Django URLs
- 변수와 URL
- App과 URL
- URL과 이름 지정
- URL 이름 공간
-----


## 1. Django Template

### 1-1. Template System
Django Template System : 데이터의 표현을 제어하면서, 표현과 관련된 부분을 담당
#### Django Template Language
Django Template Language(DTL) : Template에서 조건, 반복, 변수 등 프로그래밍적 기능을 제공하는 시스템

- Django Documentation의 'Built-in template tags and filters'에서 확인


#### DTL Syntax
1. Variable
- render 함수의 세 번째 인자로 딕셔너리 데이터를 사용
- 딕셔너리의 key에 해당하는 문자열이 곧 template에서 사용 가능한 변수명
- {{ variable }}
- dot(.)을 사용하여 변수 속성에 접근 가능
2. Filters
- 표시할 변수를 수정해야 할 경우 사용
- chained가 가능 / 일부 필터는 인자를 받기도 함
- 약 60개의 built-in template filters 제공
- {{ variable|filter }}와 같은 방법으로 사용
3. Tags
- 반복 또는 논리를 수행하여 제어 흐름을 만드는 법
- 일부 태그는 시작, 종료 태그가 필요
- 약 24개의 built-in template tags 제공
- {% tag %}와 같은 방법으로 사용
  - ex. {% if %} {% endif %}
4. Comments
- 주석처리
- {# name #}
- {% comment %} {% endcomment %}사이에 있는 모든 내용을 주석 처리

### 1-2. 템플릿 상속
기본 템플릿 구조의 한계
- 만약 모든 템플릿에 bootstrap을 적용하려면??? 템플릿이 100개인데....
- 이런 경우, 모든 템플릿에 bootstrap CDN을 작성해야 하는가??
- 상속을 시키면 편하겠군
#### 템플릿 상속
템플릿 상속(Template inheritance) : 페이지의 공통 요소를 포함하고, 하위 템플릿이 재정의할 수 있는 공간을 정의하는 기본 스켈레톤 템플릿을 작성하여 상속 구조를 구축하는 것

### 1-3. HTML form(요청과 응답)
HTML form : HTTP 요청을 서버에 보내는 가장 편한 방법
- HTML form element를 통해 사용자와 애플리케이션 간의 상호작용을 이해해야 한다
form : 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러 방식
  - text, password, checkbox 등을 제공
#### form의 구성
1. action & method : form의 핵심 속성
- 데이터를 어디로(action) 어떻게(method) 요청할까요?
2. input : 사용자의 데이터를 입력받을 수 있는 요소
- name : input의 핵심 속성
  - 입력한 데이터에 붙이는 이름(key)
  - 데이터 제출 시, 서버는 name 속성에 설정된 값을 통해서만 사용자 입력 데이터에 접근 가능
  - * Query String Parameters 
    - 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 법

## 2. Django URLs
### 2-1. Django URLs
#### 현재 URL 관리의 문제점
템플릿의 많은 부분이 중복되고 URL의 일부만 변경되는 상황일 경우

### 2-2. 변수와 URL
### 2-3. App과 URL
### 2-4. URL과 이름 지정
### 2-5. URL 이름 공간