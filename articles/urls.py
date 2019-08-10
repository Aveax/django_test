from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)
# from .views import (
#     article_get_view,
#     article_create_view,
#     article_delete_view,
#     articles_list_view
# )

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view()),
    path('<int:id>/delete/', ArticleDeleteView.as_view()),
    path('<int:id>/update/', ArticleUpdateView.as_view())
]
# urlpatterns = [
#     path('', articles_list_view),
#     path('<int:id>/', article_get_view, name='article-detail'),
#     path('create/', article_create_view),
#     path('<int:id>/delete/', article_delete_view)
# ]
