from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('chats', views.ChatView.as_view()),
    path('chats/delete/<int:id>', csrf_exempt(views.ChatView.as_view())),
    path('chats/update/<int:id>', csrf_exempt(views.ChatView.as_view())),
]
