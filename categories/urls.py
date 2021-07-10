from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('category', views.CategoryView.as_view()),
    path('category/delete/<int:id>', csrf_exempt(views.CategoryView.as_view())),
    path('category/update/<int:id>', csrf_exempt(views.CategoryView.as_view())),
]
