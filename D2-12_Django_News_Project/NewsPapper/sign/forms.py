from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.models import Group


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs = {'class': 'form-control', 'placeholder': 'Email'}
        self.fields['password'].widget.attrs = {'class': 'form-control', 'placeholder': 'Пароль'}
        self.fields["login"].label = ""
        self.fields["password"].label = ""


class MySignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Email'}
        self.fields['password1'].widget.attrs = {'class': 'form-control', 'placeholder': 'Пароль'}
        self.fields['password2'].widget.attrs = {'class': 'form-control', 'placeholder': 'Пароль еще раз'}
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""

    def save(self, request):
        user = super().save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
