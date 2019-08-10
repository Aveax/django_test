from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleForm
from .models import Article

# Create your views here.


class ArticleListView(ListView):
    template_name = 'articles/articles_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:articles-list')


# def article_get_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         'object': obj
#     }
#     return render(request, "articles/article_detail.html", context)
#
#
# def articles_list_view(request):
#     queryset = Article.objects.all()
#     print(queryset)
#     context = {
#         'object_list': queryset
#     }
#     return render(request, "articles/articles_list.html", context)
#
#
# def article_create_view(request):
#     form = ArticleForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ArticleForm()
#     context = {
#         'form': form
#     }
#     return render(request, "articles/article_create.html", context)
#
#
# def article_delete_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('../../')
#     context = {
#         'object': obj
#     }
#     return render(request, "articles/article_delete.html", context)
