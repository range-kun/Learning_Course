from django.urls import path, re_path
from .views import PostsView, PostView, SearchView, CreateNews, NewsUpdateView, \
    NewsDeleteView, CategoryView, subscribe_to_category, too_much
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(PostsView.as_view())),
    path('<int:pk>', PostView.as_view(), name='single_news'),
    path('search', SearchView.as_view()),
    path('add', CreateNews.as_view(), name='create_news'),
    path('<int:pk>/edit', NewsUpdateView.as_view(), name='update_news'),  # name нужен что бы
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='delete_news'),  # обращаться к ним через %url
    path('category/<str:category>', cache_page(300)(CategoryView.as_view()), name='category_url'),
    re_path(r'subscribed', subscribe_to_category, name='subscribed'),
    path('too_much', too_much)
]
