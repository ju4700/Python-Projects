from django.urls import path
from . import views
from .views import api_task_detail, api_task_list

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
]
urlpatterns += [
    path('api/tasks/', api_task_list, name='api_task_list'),
    path('api/tasks/<int:task_id>/', api_task_detail, name='api_task_detail'),
]