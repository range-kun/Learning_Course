from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .filters import PostFilter
from .forms import NewsForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from accounts.models import Author
from datetime import datetime
from django.core.cache import cache

User = get_user_model()

# Create your views here.


class PostsView(ListView):
    model = Post
    template_name = r'news/news.html'
    context_object_name = 'news'
    queryset = Post.objects.all().order_by('-date_of_creation')
    paginate_by = 10


class SearchView(ListView):
    model = Post
    template_name = r'news/search.html'
    context_object_name = 'search'
    ordering = ['-date_of_creation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostView(LoginRequiredMixin, DetailView):
    template_name = r'news/single_news.html'
    context_object_name = 'single_news'
    queryset = Post.objects.all()

    def get_object(self, queryset=None):
        obj = cache.get(f'news-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=queryset)
            cache.set(f'news-{self.kwargs["pk"]}', obj)
        return obj


class CreateNews(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    template_name = r'news/create_news.html'
    form_class = NewsForm

    def post(self, request, *args, **kwargs):
        author = Author.objects.get(user__id=request.POST['author'])
        today = datetime.today().strftime('%d')
        posts_for_today = Post.objects.filter(author=author, date_of_creation__day=today)
        if len(posts_for_today) > 2:
            return redirect('/news/too_much')
        else:
            post = Post(
                author=author,
                text_content=request.POST['text_content'],
                header=request.POST['header'],
                type_of_content=request.POST['type_of_content'],
            )
            post.save()
            post.category.set(request.POST.getlist('category'))
            return redirect(post.get_absolute_url())


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    template_name = r'news/create_news.html'
    form_class = NewsForm

    def get_object(self, **kwargs):  # нужен для получения записи с возможностью редактирования
        idi = self.kwargs.get('pk')
        return Post.objects.get(pk=idi)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    queryset = Post.objects.all()
    permission_required = ('news.delete_post')
    success_url = '/news/'
    template_name = r'news/delete_news.html'
    context_object_name = 'delete_in_view'


class CategoryView(ListView):
    model = Post
    template_name = r'news/news_by_category.html'
    slug_field = 'category'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super(CategoryView, self).get_queryset()
        return queryset.filter(category__category=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs['category']
        context['category'] = category.capitalize()
        user = User.objects.get(username=self.request.user)
        if not user.category:
            context['is_not_subscribed'] = True
        return context


def subscribe_to_category(request):
    category = request.GET.get('category')
    user = User.objects.get(id=request.user.id)
    if not user.category:
        category_instance = Category.objects.get(category=category)
        user.category = category_instance
        user.save()
    args = {
        'category': category
    }
    return render(request, r'news/subscribed.html', args)


def too_much(request):
    return render(request, r'news/limit_exceeded.html')
