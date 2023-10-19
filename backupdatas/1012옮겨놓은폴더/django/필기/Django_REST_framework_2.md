# Django REST framework - 2

## 목차
1. DRF with N:1 Relation
2. 역참조 데이터 구성
3. API 문서화

## 1. DRF with N:1 Relation
### 사전 준비
1. Comment 모델 정의
```python
# 1-1. Comment 클래스 정의 및 데이터 베이스 초기화
# articles/models.py
class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
# 1-2. Migration 및 fixtures 데이터 로드
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata articles.json comments.json 
```
2. URL 및 HTTP request method 구성
- URL : comments/ -> GET(댓글 목록 조회)
- URL : comments/<int:comment_pk> -> GET(단일 댓글 조회), PUT(단일 댓글 수정), DELETE(단일 댓글 삭제)
- URL : articles/<int:article_pk>/comments/ -> POST : 댓글 생성
### GET
댓글 목록 조회를 위한 CommentSerializer 정의(QuerySet을 json으로 변경 불가 -> Serializer 사용)
1. 댓글 목록 조회
2. 단일 댓글 조회
### POST
#### 

### 응답 데이터 재구성
사용자 입장에서, "article" : 20 - 이것이 무엇을 의미하는지 정확히 파악이 힘듬
- 댓글 조회 시, 게시글 번호만 제공하는 것이 아닌, 게시글의 제목까지 제공
- Serializer을 내부에서 추가 선언
```python
#articles/serializers.py
class CommentSerializer(serializers.ModelSerializer):
  # 내부에서 새로운 Serialzier 선언
  class ArticleTitleSerializer(serializers.ModelSerializer):
    class Meta:
      model = Article
      fields = ('title',)
  # 안에서 새롭게 정의한 Serializer에서 생성한 값을 읽기전용으로 하여 인스턴스 변수에 저장
  article = ArticleTitleSerializer(read_only=True) # read_only=True를 설정하지 않을 경우, 아래 Meta에서 read_only_fields 가 실행되지 않음(덮어씌워지기 때문)
  class Meta:
      model = Comment
      fields = '__all__'
      # read_only_fields = ('article', )
```
## 2. 역참조 데이터 구성
### Article -> Comment
Article(1) -> Comment(N) 간 역참조 관계를 활용한 JSON 데이터 재구성
- 단일 게시글 조회 시, 해당 게시글에 작성된 댓글 목록 데이터도 함께 붙여서 응답
- 단일 게시글 조회 시, 해당 게시글에 작성된 댓글 개수 데이터도 함께 붙여서 응답
#### 역참조 데이터 구성
1. 단일 게시글 + 댓글 목록 : Nested relationships
- 모델 관계 상으로 참조하는 대상은 참조되는 대상의 표현에 포함되거나 중첩 가능
- 이러한 중첩 관계를 serializers 필드로 표현 가능
```python
class ArticleSerializer(serializers.ModelSerializer):
  # 내부에서 사용할 Serializer 클래스 생성
  class CommentSerializer(serializers.ModelSerializer):
    # 어쩌고 저쩌고 .....
  # 역참조 related manager 이름에 Queryser을 변환한 값 저장
  # QuerySet -> many=True / 읽기 전용 -> read_only=True
  comment_set = CommentSerializer(many=True, read_only=True)
```
2. 단일 게시글 + 댓글 개수 : 댓글 개수에 해당하는 새로운 필드 생성
```python
class ArticleSerializer(serializers.ModelSerializer):
  comment_set = CommentSerializer(many=True, read_only=True)
  # 댓글 개수를 새주는 새로운 필드 생성
  comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
```
## 3. API 문서화