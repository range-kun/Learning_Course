from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class UpdateUserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Email'}
        self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder': 'Username'}
        self.fields['first_name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Имя'}
        self.fields['last_name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Фамилия'}

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
