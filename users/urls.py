from django.urls import path
from .views import Register, Login, UserView, Logout

urlpatterns = [
    path('user/register', Register.as_view()),
    path('user/login', Login.as_view()),
    path('user', UserView.as_view()),
    path('user/logout', Logout.as_view())
]
