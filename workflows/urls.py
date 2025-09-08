from django.urls import path

from .views import (
    index_view,
    read_more_view,
    home_view,
    WorkersViewList,
    TasksViewList,
    TaskViewCreate
)

urlpatterns = [
    path('', index_view, name="index"),
    path('readmore/', read_more_view, name="read-more"),
    path('home/', home_view, name='home-view'),
    path('home/workers/', WorkersViewList.as_view(), name='workers-list'),
    path('home/tasks/', TasksViewList.as_view(), name='tasks-list'),
    path('home/task-create/', TaskViewCreate.as_view(), name='task-create')
]

app_name = 'workflows'