from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import TaskType, Position, Worker, Task

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    model = Worker
    list_display = UserAdmin.list_display + ('position',)
    list_filter = UserAdmin.list_filter + ('position',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline', 'is_completed', 'priority', 'task_type')
    list_filter = ('is_completed', 'priority', 'task_type')
    search_fields = ('name', 'description')

admin.site.unregister(Group)
