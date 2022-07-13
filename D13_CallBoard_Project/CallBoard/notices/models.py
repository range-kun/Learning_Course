from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from .utils import generate_unique_name


User = settings.AUTH_USER_MODEL

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Notice(models.Model):
    header = models.CharField(max_length=255)
    text_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notice')
    date_of_creation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('single_notice', args=(self.pk,))

    def __str__(self):
        return self.header


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='reply')
    text = models.TextField(default='Готов помочь!')
    accepted = models.BooleanField(null=True)

    def is_not_proceed(self):
        return self.accepted is None

    def __str__(self):
        return self.text[:20]


class Video(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='video')
    video_file = models.FileField(upload_to=generate_unique_name('videos/'))

    def is_photo(self):
        return False


class Image(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='photo', null=True)
    image_file = models.FileField(upload_to=generate_unique_name('photos/'))

    def is_photo(self):
        return True
