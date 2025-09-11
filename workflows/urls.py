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
    TaskDeleteView,
    WorkerDetailView,
    MyProjectsListView,
    MyTeamsListView,
    ProjectCreateView,
    TeamCreateView,
    ProjectDetailView,
    TeamDetailView
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
    path('home/<int:pk>/task-delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('home/<int:pk>/worker/', WorkerDetailView.as_view(), name='worker-detail'),
    path('home/my-projects/', MyProjectsListView.as_view(), name='my-project-list'),
    path('home/my-teams/', MyTeamsListView.as_view(), name='my-team-list'),
    path('home/project-create/', ProjectCreateView.as_view(), name='project-create'),
    path('home/team-create/', TeamCreateView.as_view(), name='team-create'),
    path('home/<int:pk>/project/', ProjectDetailView.as_view(), name='project-detail'),
    path('home/<int:pk>/team/', TeamDetailView.as_view(), name="team-detail" )
]

app_name = 'workflows'