from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
# 단일 데이터 조회하는 코드에 사용
from django.shortcuts import get_object_or_404, get_list_or_404

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 일부분에 대한 수정 -> partial=True 인자 사용
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 목록 조회
@api_view(['GET'])
def comment_list(request):
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    # QuerySet -> many=True를 인자로 삽입(앞이 다중 데이터 -> True)
    serializer = CommentSerializer(comments, many=True) 

    return Response(serializer.data) # json데이터 반환

# 단일 댓글 관련 함수
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 단일 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # 단일 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 단일 댓글 수정
    elif request.method == 'PUT':
        # 댓글 : content만 수정할 수 있음 -> partial 지정 X
        serializer = CommentSerializer(comment, data=request.data)
        # 유효성 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 특정 게시글에 댓글 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    # request.data에 댓글이 포함되어있음
    serializer = CommentSerializer(data=request.data)

    # 유효성 검사 성공
    # raise_exception=True : 뭔가 잘못되었을 때, 에러를 반환해줌
    # 원래는 오류 발생 : serializer에 유효성 검사 이후 article을 부여 -> is_valid가 False
    # 이를 방지하기 위해, serializers.py에서 읽기 전용 필드로 설정
    if serializer.is_valid(raise_exception=True):
        # 저장 후, 결과 반환
        # drf의 commit=False의 역할
        # db에 보내기 전, article에 인스턴스 저장 후 save
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)