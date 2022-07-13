from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Author
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


class UserView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = r'accounts/user_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context


class UpdateUserView(UpdateView):
    template_name = r'accounts/user_update.html'
    success_url = f'/news/'
    form_class = UpdateUserForm

    def get_object(self, **kwargs):  # нужен для получения записи с возможностью редактирования
        idi = self.kwargs.get('pk')
        return User.objects.get(pk=idi)


@login_required
def become_author(request):
    user = request.user
    author_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        author_group.user_set.add(user)
    new_author = Author.objects.create(user=user)
    return render(request, r'accounts/upgraded.html')
