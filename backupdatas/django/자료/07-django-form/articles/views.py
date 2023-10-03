from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    # 요청의 메서드가 POST라면 (create)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사 진행
        # 유효성 검사가 통과된 경우
        if form.is_valid():
            article = form.save() # form 인스턴스 저장
            # 재요청
            return redirect('articles:detail', article.pk)
    # 요청의 메서드가 POST가 아니라면 (new)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    # 렌더링 페이지 리턴(is_valid()가 False일 때 발생하는 에러 메시지와 함께)
    return render(request, 'articles/create.html', context)
    
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 요청의 메서드가 POST라면 (update)
    if request.method == 'POST':
        # instance 포함해주는 이유 : 수정(생성은 X)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save() # 생성인지 수정인지 구분해야 함!!
            return redirect('articles:detail', article.pk)
    # 요청의 메서드가 POST가 아니라면 (edit)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
