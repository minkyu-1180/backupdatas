# Fundamentals of HTML and CSS

## 목차
#### 1. 웹 소개
#### 2. 웹 구조화
- HTMl
- HTML의 구조
- 텍스트 구조
#### 3. 웹 스타일링
- CSS
- CSS 선택자
- 우선순위 


## 1. 웹 소개
<웹 관련 용어>
1. World Wide Web(WWW) : 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
2. Web : Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술
3. Web site : 인터넷에서 여러 개의 Web page가 모인 것
- 사용자들에게 정보나 서비스를 제공하는 공간
4. Web page : HTML, CSS 등의 웹 기술을 이용하여 만들어진 것
Web site를 구성하는 하나의 요소

### Web page의 구성 요소
![Alt text](<웹페이지의 구성 요소-1.png>)

## 2. 웹 구조화

### HTML
HTML(HyperText Markup Language) : 웹 페이지의 의미와 구조를 정의하는 언어
- HyperText : 웹 페이지를 다른 페이지로 연결하는 링크
  - 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
  - ex) HTML, Markdown

### HTML의 구조
![Alt text](<HTML의 구조-1.png>)
```python
'''
<!DOCTYPE html> : 해당 문서가 html로 문서라는 것을 나타냄
<html></html> : 전체 페이지의 콘텐츠 포함
<title></title> : 브라우저 탭 및 즐겨찾기 시 표시되는 제목
<head></head> : HTML 문서에 관련된 설명, 설정 등 사용자에게 보이지 않는 부분
<body></body> : 페이지에 표시되는 모든 컨텐츠
'''
```

#### HTML의 요소
![Alt text](<HTML의 요소-1.png>)

HTML의 하나의 요소는 여는 태그<>와 닫는 태그</>, 그리고 그 안의 내용으로 구성된다
- 닫는 태그가 없는 태그도 존재(그 자체로 역할이 있는 것)

#### HTML의 속성
![Alt text](<HTML의 속성-1.png>)

규칙
- 속성은 요소 이름과 속성 사이에 공백이 있어야 함
- 하나 이상의 속성들이 있는 경우, 속성 사이에 공백으로 구분
- 속성 값은 열고 닫는 따옴표로 감싸야 함
목적
- 나타내고 싶지 않지만, 추가적인 기능, 내용을 담고 싶을 때 사용
- CSS에서 해당 요소를 선택하기 위한 값으로 활용

#### HTML의 텍스트 구조
HTML의 주요 목적 중 하나 : 텍스트 구조와 의미를 제공하는 것

<대표적인 HTML Text Structure>
![Alt text](<web_png/대표적인 HTMl 텍스트 구조.PNG>)
- Heading & Paragraphs(h1 ~ h6, p)
- Lists(ol, ul, li)
  - ol : 정렬된 리스트(ordered list) -> 숫자가 붙여서 출력
  - ul : 정렬되지 않은 리스트(unordered list) -> 검은 점을 붙여서 출력
  - li : 리스트
- Emphasis & Importance
  - em : 기울여진 글씨체
  - strong : 진한 글씨체

#### HTML의 사소한 특징
- 두 칸 들여쓰기
  - 들여쓰기가 필수는 아니지만, 구분을 위해 해주는 것이 좋다
- 디버깅이 힘들다 -> 개발자 도구를 항상 확인해야 하는 이유

## 3. 웹 스타일링

### CSS
CSS(Cascading Style Sheet) : 웹 페이지의 디자인과 레이아웃을 구성하는 언어

<CSS의 구성요소>
![Alt text](<web_png/CSS의 구성요소.PNG>)

ex. h1의 구문을 색상을 red로, font-size를 30px로 할 것이다.
- 선택자를 하나 선택하여, 각 속성에 알맞는 값을 선언한다.

#### CSS 적용 방법
1. 인라인(Inline) 스타일 : HTML 요소 안에 style 속성 값으로 작성
   - ![Alt text](<web_png/CSS 적용 방법 - 인라인 스타일.PNG>)
2. 내부(Internal) 스타일 : head 태크 안에 style 태그에 작성
   - ![Alt text](<web_png/CSS 적용 방법 - 인터널 스타일.PNG>)
3. 외부(Externa) 스타일 : 별도의 CSS 파일 생성 후, HTMl link 태그를 사용해 불러오기
   - ![Alt text](<web_png/CSS 적용 방법 - 익스터널 스타일.PNG>)


### CSS Selectors
CSS 선택자 : HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

#### CSS Selectors의 종류
<기본 선택자>
1. 전체(*) 선택자 : HTML의 모든 요소 선택
2. 요소(tag) 선택자 : 지정한 모든 태그 선택
3. 클래스(class) 선택자(.) : 주어진 클래스 속성을 가진 모든 요소 선택
4. 아이디(id) 선택자(#) : 주어진 아이디 속성을 가진 요소 선택
   - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함(여러개 있어도 적용은 되지만, 기능상의 문제점 발생)
5. 속성(attr) 선택자

<결합자>
1. 자손 결합자(" ") : 선택한 요소의 모든 하위 요소들을 선택
  - ex. p span : p 요소 안에 있는 모든 span을 선택(하위 레벨 상관 X)
2. 자식 결합자(">") : 선택한 요소의 한 단계 아래(직계 자식)만 선택
   

*** 주의사항 ***
- 클래스 선택자를 가장 많이 활용(재사용성, 우선순위)

### 우선순위
우선순위(Specificity) : 동일한 요소에 적용 가능한 스타일을 두 가지 이상 작성했을 시, 어떤 규칙이 적용되는 지 결정하는 것
- CSS : Cascading(계단식) -> 동일한 우선순위를 갖는 규칙이 적용될 때, CSS에서 마지막에 나오는 규칙이 사용됨

<우선순위>
1. Importance(!importance)
2. Inline 스타일(이걸 안 쓰는 이유 - 태그 안에 작성하기 때문에 우선순위가 너무 높아짐)
3. 선택자 : id > class > 요소
4. 소스 코드 순서(cascade)

### 상속
CSS 상속 : 부모 요소의 속성을 자식에게 상속하여 재사용성을 높이는 것
#### 상속 여부
1. 상속 되는 속성 : Text 관련 요소(font, color, text-align), opacity, visibility 등
2. 상속되지 않는 속성 : 
   - Box model 관련 요소
   - position 관련 요소