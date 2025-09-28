from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TaskForm, FilterTask, ProjectForm, TeamForm
from .mixins import ProjectManagerRequiredMixin
from .models import Worker, Task, Project, Team


def index_view(request) -> HTTPResponse:
    return render(request, "index.html")

def read_more_view(request) -> HTTPResponse:
    return render(request, "read_more.html")

def home_view(request) -> HTTPResponse:
    return render(request,"home.html")

class WorkersViewList(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "workers_list.html"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = 'worker-detail.html'


class TasksViewList(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task-list.html"
    def post(self,request ,*args, **kwargs):
        task_pk = request.POST.get("pk" or None)
        if task_pk:
            task = Task.objects.get(pk=task_pk)
            task.is_completed = not task.is_completed
            task.save()
        return  redirect("workflows:tasks-list")

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search_form"] = FilterTask
        if self.request.GET:
            context["search_form"] = FilterTask(self.request.GET)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        priority = self.request.GET.get("priority")
        deadline = self.request.GET.get("deadline")
        task_type = self.request.GET.get("task_type")

        if priority:
            qs = qs.filter(priority=priority)
        if task_type:
            qs = qs.filter(task_type__name=task_type)
        if deadline:
            if deadline == "asc":
                qs = qs.order_by("deadline")
            elif deadline == "desc":
                qs = qs.order_by("-deadline")

        return qs



class TaskViewCreate(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task-create-&-update.html'
    success_url = reverse_lazy("workflows:tasks-list")


class MyTasksViewList(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task-list.html"

    def get_queryset(self):
        return Worker.objects.get(pk=self.request.user.pk).tasks.all()

    def post(self, request, *args, **kwargs):
        task_pk = request.POST.get("pk" or None)
        if task_pk:
            task = Task.objects.get(pk=task_pk)
            task.is_completed = not task.is_completed
            task.save()
        return  redirect("workflows:my-tasks-list")

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search_form"] = FilterTask
        if self.request.GET:
            context["search_form"] = FilterTask(self.request.GET)
        return context



class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task-create-&-update.html"
    success_url = reverse_lazy("workflows:tasks-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "task-delete.html"
    success_url = reverse_lazy("workflows:tasks-list")


class MyProjectsListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "my-project-list.html"
    context_object_name = 'projects'

    def get_queryset(self):
        user_teams = self.request.user.teams.all()
        return Project.objects.filter(teams__in=user_teams).distinct()


class MyTeamsListView(LoginRequiredMixin, generic.ListView):
    model = Team
    template_name = "my-team-list.html"


class ProjectCreateView(ProjectManagerRequiredMixin, generic.CreateView):
    model = Project
    template_name = "project-create.html"
    form_class = ProjectForm
    success_url = reverse_lazy("workflows:home-view")

class TeamCreateView(ProjectManagerRequiredMixin, generic.CreateView):
    model = Team
    template_name = "team.create.html"
    form_class = TeamForm
    success_url = reverse_lazy("workflows:home-view")


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = 'project-detail.html'


class TeamDetailView(LoginRequiredMixin,generic.DetailView):
    model = Team
    template_name = "team-detail.html"

