from django.urls import path
from .views import (
    Tasklist,
    Taskdetail,
    Tasknew,
    Taskupdate,
    Taskdelete,
    CompleteTaskView,
)
urlpatterns = [
    path('', Tasklist.as_view(), name='task_list'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='task_detail'),
    path('task/new/', Tasknew.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', Taskupdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', Taskdelete.as_view(), name='task_delete'),
    path('task/<int:pk>/complete/', CompleteTaskView.as_view(), name='task_complete'),
]
