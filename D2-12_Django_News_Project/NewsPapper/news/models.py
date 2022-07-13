from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.core.cache import cache

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    category = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.category.title()


class Post(models.Model):
    NEWS = 'NEWS'
    POST = 'POST'
    type_choice = [(NEWS, 'Новость'), (POST, 'Пост')]

    author = models.ForeignKey('accounts.Author', on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    text_content = models.TextField()
    rating = models.IntegerField(default=0)
    header = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, through='PostCategory')
    type_of_content = models.CharField(max_length=4, choices=type_choice, default=NEWS)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'news-{self.pk}')

    def get_absolute_url(self):
        return reverse('single_news', args=(self.pk,))  # нужен для редиректа после создания или изменения

    def __str__(self):
        return f'{self.header.title()}: {self.preview()}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def categories(self):
        return '\n'.join(news.category for news in self.category.all())

    def header_preview(self):
        return self.header[:15]

    def preview(self):
        return f'{self.text_content[:50]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text_of_comment = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __st__(self):
        return self.preview()

    def preview(self):
        return self.text_of_comment[:15]

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

