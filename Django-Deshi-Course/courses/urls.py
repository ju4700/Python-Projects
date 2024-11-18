from django.urls import path
from . import views
from .views_auth import register_view, login_view, logout_view

urlpatterns = [
    path('', views.home, name='home'),
]
urlpatterns += [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
