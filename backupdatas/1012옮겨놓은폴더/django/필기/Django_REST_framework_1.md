# Django REST Framework - 1

## 목차
1. REST API
2. DRF
3. DRF with Single Model

## 1. REST API
### REST API
API(Application Programming Interface) : 애플리케이션과 프로그래밍으로 소통하는 법
- 클라이언트 <-> 서버 처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계
REST(Representational State Transfer) : API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- 자원을 정의하고, 자원에 대한 주소를 지정하는 전반적인 방법 서술
REST API : REST 설계 디자인을 지켜(RESTful) 구현한 API
#### REST의 자원 정의/주소 지정 방법
1. 자원의 식별 : URI
2. 자원의 행위 : HTTP Methods
3. 자원의 표현 : JSON 데이터
- 궁극적으로 표현되는 데이터 결과물
### 자원의 식별 : URI
URI(Uniform Resource Identifier) : 통합 자원 식별자
- 인터넷에서 리소스(자원)를 식별하는 문자열
- 가장 일반적인 URI : URL(웹 주소)
URL(Uniform Resource Locator) : 통합 자원 위치
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어디 있는지 알려주기 위한 약속
#### Schema(or Protocol)
http(Scheme)://www.example.com(Domain Name):80(Port)/path/to/myfile.html(Path to the file)?key1=value1&key2=value2(Parameters)#SomewhereInTheDocument(Anchor)
1. Schema : 브라우저가 리소스를 요청하는 데 사용해야 하는 규약
- URL의 첫 부분 : 브라우저가 어떤 규약을 사용하는지를 나타냄
- 웹은 기본적으로 HTTP(S)를 요구하며, 메일을 열기 위한 mailto:, 파일을 전송하기 위한 ftp: 등 다른 프로토콜도 존재
2. Domain Name : 요청중인 웹 서버
- 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능하지만, 사람이 외우기 어렵기 때문에 주로 Domain Name으로 사용
  - ex. google.com 도메인의 IP 주소 : 142.251.42.142
3. Port : 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
- HTTP 프로토콜의 표준 포트 : 80
- HTTPS 프로토콜의 표준 포트 : 443
- 표준 포트만 생략 가능
4. Path : 웹 서버의 리소스 경로
- 초기 : 실제 파일이 위치한 물리적 위치
- 요즘 : 실제 위치가 아닌, 추상화된 형태의 구조 표현
  - ex. /articles/create/ : 실제 articles 폴더 안에 존재하는 create 폴더의 안을 의미하는 것이 아닌, 추상적인 구조 표현
5. Parameters : 웹 서버에 제공하는 추가적인 데이터
- '&' 기호로 key-value 쌍 구분
- 서버는 리소스를 응답하기 전, 파라미터를 사용하여 추가 작업을 수행
6. Anchor : 일종의 북마크를 나타내며, 브라우저에 해당 지점이 있는 콘텐츠를 표시
- fragment identifier(부분 식별자)라고 부르는 '#' 이후 부분은 서버에 전송되지 않음(#앞에 부분까지만 요청 -> 브라우저가 anchor 처리(화면 이동))

### 자원의 행위 : HTTP Methods
HTTP Request Methods : 리소스에 대한 행위(수행하고자 하는 동작)를 정의(= HTTP verbs)
1. GET
- 서버에 리소스의 표현 요청
- 데이터 검색
2. POST
- 데이터를 지정된 리소스에 제출
- 서버 상태 변경
3. PUT
- 요청한 주소의 리소스를 수정
4. DELETE
- 지정된 리소스 삭제
HTTP Response status Codes : 특정 요청이 성공적으로 완료 되었는지에 대한 여부
1. Informational responses(100-199)
2. Successful responses(200-299)
3. Redirection messages(300-399)
4. Client error responses(400-499)
5. Server error responses(500-599) 
   
### 자원의 표현
지금까지 응답 방식 : Django 서버는 사용자에게 html만 응답
- 페이지 외의 다양한 데이터 타입을 응답 가능
- RESP API : JSON 타입으로 응답하는 것을 권장