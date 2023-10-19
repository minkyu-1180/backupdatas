from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
    article = ArticleTitleSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        # 읽기 전용 필드
        # 조회시에는 필요 / 유효성 검사는 제외
        # read_only_fields = ('article', )

class ArticleSerializer(serializers.ModelSerializer):
    # 시행할 함수를 source='문자열'로 작성
    # article 인스턴스        
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # 다중 데이터 -> many=True
    # 사용자로부터 입력받는 데이터가 아님(유효성 검사 필요 X) -> read_only=True
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

