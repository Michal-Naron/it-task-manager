from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    NAME_CHOICES = [
        ('bug', 'Bug'),
        ('new_feature', 'New feature'),
        ('breaking_change', 'Breaking change'),
        ('refactoring', 'Refactoring'),
        ('qa',"QA")
    ]
    name = models.CharField(
        max_length=255,
        choices=NAME_CHOICES,
        default='new_feature'
    )

    def __str__(self):
        return self.get_name_display()


class Position(models.Model):
    NAME_CHOICES = [
        ('developer','Developer'),
        ('project_manager', 'Project manager'),
        ('qa', 'QA'),
        ('designer', 'Designer'),
        ('devops', 'DevOps')
    ]

    name = models.CharField(
        max_length=255,
        choices=NAME_CHOICES
    )

    def __str__(self):
        return self.get_name_display()

class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name='workers',
        null = True,
        blank = True
    )

    def __str__(self):
        return f"{self.username} Position: {self.position}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    assignees = models.ManyToManyField("Worker", related_name="teams")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    teams = models.ManyToManyField(Team, related_name="projects")

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('urgent', 'Urgent'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=255,
        choices=PRIORITY_CHOICES
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name='tasks')
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} deadline: {self.deadline} priority: {self.get_priority_display()}"