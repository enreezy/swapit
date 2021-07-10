from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('posts', views.PostView.as_view()),
    path('posts/delete/<int:id>', csrf_exempt(views.PostView.as_view())),
    path('posts/update/<int:id>', csrf_exempt(views.PostView.as_view())),
]
