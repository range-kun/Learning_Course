from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import *
from .forms import NoticeFullForm, ReplyForm
from django.db import transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from distutils.util import strtobool
from .utils import get_content

User = get_user_model()


class NoticesView(ListView):
    model = Notice
    context_object_name = 'notices'
    template_name = r'notices/notices.html'
    queryset = Notice.objects.all().order_by('-date_of_creation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['1_photo'] = Image.objects.first()
        return context


class NoticeView(DetailView):
    template_name = r'notices/notice.html'
    context_object_name = 'notice'
    queryset = Notice.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context = get_content(obj, context)
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            author = obj.author
            context['is_author'] = author == user
            context['is_not_replied'] = not obj.reply.filter(user=self.request.user).exists()
        context['replies'] = obj.reply.all()
        return context


class NoticeDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Notice.objects.all()
    success_url = '/notices/'
    template_name = r'notices/delete_notice.html'
    context_object_name = 'delete'


class UpdateNoticeView(LoginRequiredMixin, UpdateView):
    template_name = 'notices/create.html'
    form_class = NoticeFullForm

    def get_object(self, **kwargs):
        idi = self.kwargs.get('pk')
        return Notice.objects.get(pk=idi)


@login_required
def create(request):
    if request.method == 'GET':
        c = {'form': NoticeFullForm()}
        return render(request, 'notices/create.html', c)
    elif request.method == 'POST':
        notice_form = NoticeFullForm(request.POST or None, request.FILES or None)
        if notice_form.is_valid():
            header = notice_form.cleaned_data['header']
            text_content = notice_form.cleaned_data['text_content']
            author = request.user
            category = notice_form.cleaned_data['category']
            with transaction.atomic():
                notice = Notice.objects.create(header=header, text_content=text_content,
                                               author=author, category=category)
                for image in request.FILES.getlist('images'):
                    Image.objects.create(notice=notice, image_file=image)
                for video in request.FILES.getlist('videos'):
                    Video.objects.create(notice=notice, video_file=video)
        return redirect(notice.get_absolute_url())


class CreateReplyView(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'notices/create_reply.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notice = Notice.objects.get(pk=self.kwargs['pk'])
        context['notice'] = notice
        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        notice = Notice.objects.get(pk=kwargs['pk'])
        text = request.POST['text']
        Reply.objects.create(user=user, notice=notice, text=text)
        return HttpResponseRedirect(notice.get_absolute_url())


def proceed_reply(request, pk):
    reply = Reply.objects.get(pk=pk)
    result = strtobool(request.GET.get('result'))
    if reply.accepted is None:
        reply.accepted = result
        reply.save()
    args = {
        'reply': reply
    }
    return render(request, 'notices/proceed_reply.html', args)
