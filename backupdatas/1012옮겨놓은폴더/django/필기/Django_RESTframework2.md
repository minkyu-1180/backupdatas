# Django
## Django REST framework 2

## 목차
1. DRF with N:1 Relation
2. 역참조 데이터 구성
3. API 문서화

## 1. DRF with N:1 Relation
### 사전 준비
1. Comment 클래스 정의 및 데이터베이스 초기화
```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auth_now_add=True)
    updated_at = models.DateTimeField(auth_now=True)
```
2. migration 및 fixtures 데이터 로드
- python manage.py makemigrations
- python manage.py migrate
- python manage.py loaddata articles.json comments.json
### GET
1. 댓글 목록 조회를 위한 CommentSerializer 정의
2. url 작성 및 view 함수 작성
- 전체 댓글 조회
- 단일 댓글 조회
```python
# articles/serializers.py
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerizliaer):
    class Meta:
        model = Comment
        fields = '__all__'

# articles/urls.py
urlpattersn = [
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),

]
# articles/views.py
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = Comments.objects.get(pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
```

### POST
- CommentSerializer에서 읽기 전용 필드 생성
    - read_only_fields : 유효성 검사에서 제외/데이터 조회시에는 출력
- 단일 댓글 생성

```python
# articles/serializers.py
class CommentSerializer(serializer.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # 유효성 검사에서 제외된 값(save하면서 설정해주기)
        read_only_fields = ('articles')

# articles/urls.py
urlpatterns = [
    ...,
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
# articles/views.py
@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 유효성 검사 성공 -> commit=False처럼 save하면서 
        # serializer의 article값을 설정해주기
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```
### DELETE & PUT
- 단일 댓글 삭제 및 수정을 위한 view 함수 작성
```python
# articles/views.py
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```
### 응답 데이터 재구성
- 댓글 조회(comment_detail -> GET)시, 게시글 출력 내역 변경
- 댓글 조회 시 게시글 번호만 제공하는 것이 아닌, 게시글의 제목까지 출력해주기
```python
# articles/serializers.py
class CommentSerializer(serializers.ModelSerializer):
    # 내부에서 추가 선언
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
    # 내부에서 선언한 Serializer객체(article)은 조회 시에만 참조 -> read_only = True
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
```
## 2. 역참조 데이터 구성
### 역참조 관계를 활용한 JSON 데이터 재구성
1. 다일 게시글 조회 시, 해당 게시글에 작성된 댓글 목록 데이터도 함께 붙여서 응답 : Nested relationships
Nested relatonships : 모델 관계 상으로 참조하는 대상은 참조되는 대상의 표현에 포함되거나, 중첩될 수 있음
- 이러한 중첩 관계는 serializers를 필드로 사용하여 표현 가능

2. 단일 게시글 조회 시, 해당 게시글에 작성된 댓글 개수 데이터도 함께 붙여서 응답

#### 읽기 전용 필드 지정 이슈 주의점
- 특정 필드를 override 혹은 추가한 경우(read_only=True 설정), 아래의 fields 지정에서 read_only_fields는 동작 X
- 해당 필드에서 read_only키워드 인자로 작성
```python
# 1. 단일 게시글 + 댓글 목록
# articles/serializers.py
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    # 2. 단일 게시글 + 댓글 개수
    # source : 점 표기법을 사용하여 속성 탐색 가능(source='comment_set.count')
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```
## 3. API 문서화
### OpenAPI Specification
OAS(OpenAPI Specification) : RESTful API를 설명하고 시각화하는 표준화된 방법
- API에 대한 세부사항을 기술할 수 있는 공식 표준

### 참고
#### Django shortcuts functions
1. get_object_or_404() : 모델 manager objects에서 get()을 호출하지만, 해당 객체가 없을 경우 기존 DoesNotExist 예외 대신 Http404를 raise
2. get_list_or_404() : 모델 manager objects에서 filter()의 결과를 반환하지만, 해당 객체 목록이 없을 경우 Http404를 raise
#### 사용하는 이유
클라이언트에게 500 에러 메시지 전달 : 서버에 오류가 발생하여 요청 수행 불가(원인 명시 X)
- 적절한 예외 처리를 통해 보다 정확한 에러 현황 전달
```python
from django.shortcuts import get_object_or_404, get_list_or_404

# 기존
# 존재하지 않는 게시글에 대한 조회 시, 상태 코드 500 응답
article = Article.objects.get(pk=article_pk)
articles = Article.objects.all()
# 해당 메서드 사용
# 존재하지 않는 게시글에 대한 조회 시, 상태 코드 404 응답
article = get_object_or_404(Article, pk=article_pk)
articles = get_list_or_404(Article)
```