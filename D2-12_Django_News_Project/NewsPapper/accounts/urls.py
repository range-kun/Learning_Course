from django.urls import path
from .views import UserView, UpdateUserView, become_author

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>', UserView.as_view(), name='user_view'),
    path('<int:pk>/edit', UpdateUserView.as_view(), name='update_user'),
    path('upgraded/', become_author, name='become_author')
]