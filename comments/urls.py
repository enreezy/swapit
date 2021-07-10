from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('comments', views.CommentView.as_view()),
    path('comments/delete/<int:id>', csrf_exempt(views.CommentView.as_view())),
    path('comments/update/<int:id>', csrf_exempt(views.CommentView.as_view())),
]
