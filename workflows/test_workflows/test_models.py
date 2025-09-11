from django.test import TestCase
from workflows.models import TaskType, Position, Worker, Task
from django.utils import timezone


class TaskTypeModelTests(TestCase):

    def test_tasktype_str(self):
        name_for_task = 'bug'
        task_type = TaskType.objects.create(name=name_for_task)
        self.assertEqual(str(task_type), task_type.get_name_display())


class PositionModelTests(TestCase):

    def test_position_str(self):
        name_for_position = 'developer'
        position = Position.objects.create(name=name_for_position)
        self.assertEqual(str(position), position.get_name_display())


class WorkerModelTests(TestCase):

    def test_worker_str(self):
        position = Position.objects.create(name='qa')
        worker = Worker.objects.create(username='tester', position=position)
        self.assertEqual(str(worker), f"{worker.username} Position: {worker.position}")


class TaskModelTests(TestCase):

    def test_task_str(self):
        position = Position.objects.create(name='developer')
        worker = Worker.objects.create(username='dev1', position=position)
        task_type = TaskType.objects.create(name='new_feature')

        task = Task.objects.create(
            name='Implement login',
            description='Add login feature',
            deadline=timezone.now(),
            priority='high',
            task_type=task_type
        )
        task.assignees.add(worker)

        self.assertEqual(
            str(task),
            f"{task.name} deadline: {task.deadline} priority: {task.get_priority_display()}"
        )
