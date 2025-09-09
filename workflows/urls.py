from django.urls import path

from .views import (
    index_view,
    read_more_view,
    home_view,
    WorkersViewList,
    TasksViewList,
    TaskViewCreate,
    MyTasksViewList,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path('', index_view, name="index"),
    path('readmore/', read_more_view, name="read-more"),
    path('home/', home_view, name='home-view'),
    path('home/workers/', WorkersViewList.as_view(), name='workers-list'),
    path('home/tasks/', TasksViewList.as_view(), name='tasks-list'),
    path('home/task-create/', TaskViewCreate.as_view(), name='task-create'),
    path('home/my-tasks/', MyTasksViewList.as_view(), name='my-tasks-list'),
    path('home/<int:pk>/task-update/', TaskUpdateView.as_view(), name='task-update' ),
    path('home/<int:pk>/task-delete/', TaskDeleteView.as_view(), name='task-delete')
]

app_name = 'workflows'