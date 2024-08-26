from django.urls import path
from posttest.views import PostTest

urlpatterns = [
    path("", PostTest.as_view()),
]