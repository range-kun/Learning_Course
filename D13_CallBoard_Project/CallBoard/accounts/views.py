from .forms import UpdateUserForm
from django.views.generic import TemplateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from notices.filters import NoticeFilter
from notices.models import Notice


User = get_user_model()
# Create your views here.


class UserView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'accounts/personal_space.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NoticeFilter(self.request.GET, queryset=self.request.user.notice.all())
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user_info.html'
    form_class = UpdateUserForm

    def get_success_url(self):
        idi = self.object.id
        return reverse_lazy('personal_space', kwargs={'pk': idi})


