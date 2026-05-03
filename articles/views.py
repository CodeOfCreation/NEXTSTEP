from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article


def article_list(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, 'articles/list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'articles/detail.html', {'article': article})


@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            Article.objects.create(
                title=title,
                content=content,
                author=request.user,
                is_published=True,
            )
            return redirect('article_list')
    return render(request, 'articles/create.html')
