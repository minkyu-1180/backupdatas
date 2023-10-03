from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


# formfield 및 widget 활용
# https://docs.djangoproject.com/en/4.2/ref/forms/fields/
# https://docs.djangoproject.com/en/4.2/topics/forms/
# https://docs.djangoproject.com/en/4.2/ref/forms/widgets/

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        # 위젯 설정
        widget=forms.TextInput(
            # 위젯 속성 정의
            attrs={
                'class': 'my-title',
                # 기본적으로 나타날 문자열(아무것도 작성하지 않을 시)
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력해주세요.'
        }
    )

    # model 등록
    class Meta: # ModelForm의 정보 작성 위치
        model = Article
        fields = '__all__'
        # fields = ('title',) # 입력받을 데이터 필드 설정
        # exclude = ('title',) # 모델에서 포함하지 않을 필드 설정
