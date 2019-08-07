from django.urls import path

from .views import (
    article_get_view,
    article_create_view,
    article_delete_view,
    articles_list_view
)

app_name = 'articles'
urlpatterns = [
    path('<int:id>/', article_get_view, name='article-detail'),
    path('create/', article_create_view),
    path('<int:id>/delete/', article_delete_view),
    path('', articles_list_view)
]
