from .models import Category, Article


def categories(request):
    categories = Category.objects.all()
    articles_all = Article.objects.all()
    date = []
    for item in articles_all:
        date.append(item.date_pub)
    date = list(set(date))
    return {
        'categories': categories,
        'date_all': date
    }
