from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArticleForm
from .models import Article

# Create your views here.


def article_get_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        'object': obj
    }
    return render(request, "articles/article_detail.html", context)


def articles_list_view(request):
    queryset = Article.objects.all()
    print(queryset)
    context = {
        'object_list': queryset
    }
    return render(request, "articles/articles_list.html", context)


def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, "articles/article_create.html", context)


def article_delete_view(request, id):
    obj = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../../')
    context = {
        'object': obj
    }
    return render(request, "articles/article_delete.html", context)
