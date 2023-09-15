from django.urls import path
from .views import login_view, signup, dashboard, create_task
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name='login'),
    path('signup', signup, name='signup'),
    path('dashboard', dashboard, name='dashboard'),
    path('create-task', create_task, name='create_task'),
    path('logout/', LogoutView.as_view(), name='logout'),
]