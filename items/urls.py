from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('item', views.ItemView.as_view()),
    path('item/delete/<int:id>', csrf_exempt(views.ItemView.as_view())),
    path('item/update/<int:id>', csrf_exempt(views.ItemView.as_view())),
]
