from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    
    args = {'articles': articles}
    return render(request, 'articles/articlelist.html', args)


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    args = {'article':article}
    return render(request, 'articles/article_detail.html', args)

@login_required(login_url="/accounts/login")
def create_article(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_article.html', {'form':form})