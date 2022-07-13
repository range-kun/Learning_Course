# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from news.forms import PostChangeListFrom
from .models import Category, Post, Comment


class CategoryInLine(admin.TabularInline):
    model = Post.category.through


class PostAdmin(admin.ModelAdmin):
    list_display = ('header_preview', 'categories', 'author', 'rating',)
    search_fields = ('header', 'author__user__username', 'rating', 'category__category')
    list_filter = ('header', 'author__user__username', 'rating', 'category')
    inlines = (CategoryInLine,)


def delete_all_posts(modeladmin, request, queryset):
    for category in queryset:
        posts = category.post_set.all()
        for post in posts:
            post.delete()


delete_all_posts.short_description = 'Удалить все посты выбранной категории'


class CategoryAdmdin(admin.ModelAdmin):
    search_fields = ('category',)
    list_filter = ('category',)
    actions = [delete_all_posts, ]


class CommmentAdmin(admin.ModelAdmin):
    list_display = ('preview', 'user', 'rating', 'post')
    search_fields = ('text_of_comment', 'user__username', 'rating', 'post__header')


admin.site.register(Category, CategoryAdmdin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommmentAdmin)
# Register your models here.
