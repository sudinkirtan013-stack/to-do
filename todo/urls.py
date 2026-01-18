from django.urls import path
from .views import home, complete_task, delete_task
from .api_views import task_list, task_detail
from accounts.api_views import signup_api

urlpatterns = [
    # HTML pages
    path('', home, name='home'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),

    # API endpoints
    path('api/tasks/', task_list, name='task_list_api'),
    path('api/tasks/<int:pk>/', task_detail, name='task_detail_api'),
    path('api/signup/', signup_api, name='signup_api'),
]


