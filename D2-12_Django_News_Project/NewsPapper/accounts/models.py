from django.db import models
from django.contrib.auth.models import AbstractUser
from news.models import Post, Comment
from django.conf import settings


# Create your models here.


class Author(models.Model):
    rating = models.IntegerField(default=0)
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, primary_key=True)

    @staticmethod
    def update_rating(author):
        author.rating = 0
        posts = Post.objects.filter(author=author)  # все посты автора
        author.rating += sum(list(posts.values_list("rating", flat=True))) * 3  # суммарный рейтинг каждой статьи автора
        author.rating += sum(list(Comment.objects.filter(user=author.user).values_list("rating", flat=True)))
        # рейтинг всех комментов автора
        for post in posts:  # суммарный рейтинг всех комментариев к статьям автора
            author.rating += sum(list(post.comment_set.values_list("rating", flat=True)))
        author.save()

    def __str__(self):
        return self.user.username


class User(AbstractUser):
    category = models.ForeignKey('news.Category', on_delete=models.CASCADE,
                                 related_name='subscribers', null=True)

