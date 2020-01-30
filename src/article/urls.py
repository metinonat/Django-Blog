from django.urls import path,include
from article.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('create', ArticleCreateView.as_view(), name='article_create'),
    path('detail/<int:article_id>/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('detail/<int:article_id>/update', ArticleUpdateView.as_view(), name = 'article_update'),
    path('detail/<int:article_id>/delete', ArticleDeleteView.as_view(), name = 'article_delete'),
]