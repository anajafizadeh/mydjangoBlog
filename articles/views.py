from django.shortcuts import render, HttpResponse
from . import models

def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    
    args = {'articles': articles}
    return render(request, 'articles/articlelist.html', args)


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    args = {'article':article}
    return render(request, 'articles/article_detail.html', args)