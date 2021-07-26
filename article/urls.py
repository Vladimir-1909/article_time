from django.urls import path

from . import views as AV

urlpatterns = [
    path('', AV.ArticlesView.as_view(), name='home'),
    path('articlefilter/', AV.ArticleDateFilter.as_view(), name='article_date_filter'),
    path('user/<str:username>/', AV.UserAllArticleView.as_view(), name='article_all_user'),
    path('article/add/', AV.CreateArticleView.as_view(), name='article_add'),
    path('article/<str:slug>/', AV.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<str:slug>/update', AV.UpdateArticleView.as_view(), name='article_update'),
    path('article/<str:slug>/delete', AV.DeleteArticleView.as_view(), name='article_delete'),
    path('article/', AV.article_widget),


    path('category/<str:slug>/', AV.CategoryView.as_view(), name='category_detail'),
]
