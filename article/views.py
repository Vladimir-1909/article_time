from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Article, Category
from .forms import ArticleForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime


class ArticlesView(ListView):
    model = Article
    context_object_name = 'articles'
    ordering = ['-id']
    paginate_by = 3
    template_name = 'base.html'

    def get_context_data(self, **kwards):
        ctx = super(ArticlesView, self).get_context_data(**kwards)
        ctx['title'] = 'Article Time'
        return ctx


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwards):
        ctx = super(ArticleDetailView, self).get_context_data(**kwards)
        ctx['title'] = Article.objects.get(slug=self.kwargs['slug'])
        return ctx


class CategoryView(ListView):
    model = Article
    template_name = 'article/article_category.html'
    context_object_name = 'articles'
    paginate_by = 2

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return Article.objects.filter(categories=category).order_by('-id')

    def get_context_data(self, **kwards):
        ctx = super(CategoryView, self).get_context_data(**kwards)
        categories = Category.objects.get(slug=self.kwargs['slug'])
        ctx['title'] = categories
        ctx['category'] = categories
        ctx['articles_count'] = len(Article.objects.filter(categories=categories))
        return ctx


class UserAllArticleView(ListView):
    model = Article
    template_name = 'base.html'
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(avtor=user).order_by('-id')

    def get_context_data(self, **kwards):
        ctx = super(UserAllArticleView, self).get_context_data(**kwards)
        ctx['title'] = f'Статьи от пользователя {self.kwargs.get("username")}'
        return ctx


class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article/create_article.html'
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateArticleView, self).get_context_data(**kwards)
        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx


class UpdateArticleView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article/create_article.html'
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(UpdateArticleView, self).get_context_data(**kwards)
        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.avtor:
            return True
        return False


class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/'
    template_name = 'article/article_delete.html'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.avtor:
            return True
        return False

    def get_context_data(self, **kwards):
        ctx = super(DeleteArticleView, self).get_context_data(**kwards)
        ctx['title'] = 'Удаление статьи'
        ctx['btn_text_yes'] = 'Удалить статью'
        ctx['btn_text_no'] = 'Не удалять статью'
        return ctx


def article_widget(request):
    slug = request.GET.get('slug')
    article = Article.objects.filter(slug=slug).first()
    category = article.categories.first()

    return render(request, 'article/widget/article_widget.html', {
        'article': article,
        'category': category
    })


class ArticleDateFilter(ListView):
    model = Article
    template_name = 'article/includes/article_list.html'
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        date = self.request.GET.get('date')
        return Article.objects.filter(date_pub=date).order_by('-id')

    def get_context_data(self, **kwards):
        ctx = super(ArticleDateFilter, self).get_context_data(**kwards)
        ctx['title'] = f'Статьи от даты {self.request.GET.get("date")}'
        return ctx
