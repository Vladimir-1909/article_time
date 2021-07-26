from django import forms
from .models import Article, Category


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Название',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название',
        })
    )

    body = forms.CharField(
        label='Описание',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание', 'rows': '5'})
    )

    categories = forms.ModelMultipleChoiceField(
        label='Категории',
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'included-category'})
    )

    img_article = forms.ImageField(
        label='Изображение',
        required=True
    )

    date_pub = forms.DateField(
        label='Дата',
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
        })
    )

    class Meta:
        model = Article
        fields = ['title', 'body', 'categories', 'img_article', 'date_pub']
