from django.urls import path
from .views import UserView, UserUpdateView

urlpatterns = [
    path('<int:pk>/info', UserView.as_view(), name='personal_space'),
    path('<int:pk>/edit', UserUpdateView.as_view(), name='update_user_info')
]