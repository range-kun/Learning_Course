from django.urls import path
from .views import NoticesView, NoticeView, create, NoticeDeleteView, UpdateNoticeView, \
    CreateReplyView, proceed_reply

urlpatterns = [
    path('', NoticesView.as_view(), name='notices'),
    path('<int:pk>', NoticeView.as_view(), name='single_notice'),
    path('add', create, name='create'),
    path('delete/<int:pk>', NoticeDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateNoticeView.as_view(), name='update'),
    path('<int:pk>/add_reply', CreateReplyView.as_view(), name='create_reply'),
    path('<int:pk>/proceed_reply', proceed_reply, name='proceed_reply')
]
