from http.client import HTTPResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TaskForm
from .models import Worker, Task

def index_view(request) -> HTTPResponse:
    return render(request, "index.html")

def read_more_view(request) -> HTTPResponse:
    return render(request, "read_more.html")

def home_view(request) -> HTTPResponse:
    return render(request,"home.html")

class WorkersViewList(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "workers_list.html"


class TasksViewList(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task-list.html"


class TaskViewCreate(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task-create.html'
    success_url = reverse_lazy("workflows:tasks-list")

