from django.db import models
from django.shortcuts import reverse
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + str(int(time()))


class Article(models.Model):
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    categories = models.ManyToManyField('category', blank=True, related_name='articles')
    img_article = models.ImageField('img article', default='default-article.png', upload_to='article_images')
    date_pub = models.DateField('date publication', default=timezone.now)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.slug)
        super().save(*args, **kwargs)

        image = Image.open(self.img_article.path)
        resize = (425, 255)
        image.thumbnail(resize)
        image.save(self.img_article.path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


class Category(models.Model):
    title = models.CharField(max_length=50)
    img_category = models.ImageField('img category', upload_to='category_images')
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img_category.path)
        resize = (425, 255)
        image.thumbnail(resize)
        image.save(self.img_category.path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
