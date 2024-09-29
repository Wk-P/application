from django.urls import path
from notice.views import FetchAllNotice, CommentsHandle

urlpatterns = [
    path('all/', FetchAllNotice.as_view()),
    path('comments/<str:notice_id>/', CommentsHandle.as_view()),
]