from random import choices

from django import forms
from django.forms import (
    Textarea,
    DateTimeInput,
    CheckboxInput,
    Select,
    CheckboxSelectMultiple
)
from .models import (
    Task,
    TaskType,
    Worker,
    Project,
    Team
)

class TaskForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "Task name",
            "class": "form-control form-control-lg"
        })
    )
    description = forms.CharField(
        widget=Textarea(attrs={
            "placeholder": "Description",
            "class": "form-control form-control-lg",
            "rows": 4
        })
    )
    deadline = forms.DateTimeField(
        widget=DateTimeInput(attrs={
            "class": "form-control form-control-lg",
            "type": "datetime-local"
        })
    )
    is_completed = forms.BooleanField(
        required=False,
        widget=CheckboxInput(attrs={'class': 'form-check-input'})
    )
    priority = forms.ChoiceField(
        choices=Task.PRIORITY_CHOICES,
        widget=Select(attrs={'class': 'form-select form-select-lg'})
    )
    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        widget=Select(attrs={'class': 'form-select form-select-lg'})
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=CheckboxSelectMultiple()
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=Select(attrs={'class': 'form-select form-select-lg'})
    )

    class Meta:
        model = Task
        fields = '__all__'


class FilterTask(forms.Form):
    DEADLINE_CHOICES = [
        ('asc', 'Deadline ↑ (earliest first)'),
        ('desc', 'Deadline ↓ (latest first)'),
    ]

    priority = forms.ChoiceField(
        choices= [('', '--------')] + Task.PRIORITY_CHOICES,
        required=False
    )
    deadline = forms.ChoiceField(
        choices= [('', '--------')] + DEADLINE_CHOICES,
        required=False
    )
    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        required=False
    )




class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control form-control-lg",}
        ))
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=CheckboxSelectMultiple()
    )

    class Meta:
        model = Project
        fields = "__all__"
