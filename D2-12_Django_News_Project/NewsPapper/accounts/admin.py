from django.contrib import admin
from .models import Author, User
from django.contrib.auth.admin import UserAdmin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating']
    list_filter = ['user', 'rating']


admin.site.register(Author, AuthorAdmin)
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass