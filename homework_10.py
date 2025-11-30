
'''Домашнее задание: Проект "Менеджер задач" — ORM запросы

Цель:
Освоение основных операций CRUD (Create, Read, Update, Delete) на примере заданных моделей.

Создание записей:
Task:
title: "Prepare presentation".
description: "Prepare materials and slides for the presentation".
status: "New".
deadline: Today's date + 3 days.

SubTasks для "Prepare presentation":
title: "Gather information".
description: "Find necessary information for the presentation".
status: "New".
deadline: Today's date + 2 days.
title: "Create slides".
description: "Create presentation slides".
status: "New".
deadline: Today's date + 1 day.'''

from datetime import date, timedelta
from test_app.models import Task, SubTask

# 1. Создание Task
task = Task.objects.create(
    title="Prepare presentation 1",
    description="Prepare materials and slides for the presentation 1",
    status="New",
    deadline=date.today() + timedelta(days=3) #Deadline in 3 days
)
print(f"Task '{task.title} is born! Deadline at {task.deadline}")


# 2. Создание SubTask
sub1 = SubTask.objects.create(
    task=task, #Link to the parent task
    title="Gather information",
    description="Find necessary information for the presentation",
    status="New",
    deadline=date.today() + timedelta(days=2) #Deadline in 2 days
)
print(f"SubTask '{sub1.title}' ready to collect info!")


# 3. Создание SubTask 2
sub2 = SubTask.objects.create(
    task=task, #Link to the parent task
    title="Create slides",
    description="Create presentation slides",
    status="New",
    deadline=date.today() + timedelta(days=1) #Deadline in 1 day
)
print(f"SubTask '{sub2.title}' slides on the way!")

'''Чтение записей:
Tasks со статусом "New":
Вывести все задачи, у которых статус "New".
SubTasks с просроченным статусом "Done":
Вывести все подзадачи, у которых статус "Done", но срок выполнения истек.
Изменение записей:
Измените статус "Prepare presentation" на "In progress".
Измените срок выполнения для "Gather information" на два дня назад.
Измените описание для "Create slides" на "Create and format presentation slides".
Удаление записей:
Удалите задачу "Prepare presentation" и все ее подзадачи.
Оформите ответ: 
Прикрепите все выполненные запросы (код) и скриншоты с консоли к ответу на домашнее задание'''

# 4. Чтение записей — Tasks со статусом New
new_task = Task.objects.filter(status="New") # SELECT * FROM 'tasks' WHERE status = 'NEW';
print("Task with status 'New'.")
for i in new_task:
    print(f"Task {i.title} -Status: {i.status} - Deadline: {i.deadline}")

# 5. Чтение записей — SubTasks Done + просроченные
done_subtasks = SubTask.objects.filter(
    status="Done",
    deadline__lt=date.today()
)
print("SubTasks done but overdue")

#6. Обновление — изменить статус Task
task = Task.objects.get(title="Prepare presentation 1")
task.status = "In progress"
task.save()

#7. Обновление — изменить дедлайн SubTask 1
sub1 = SubTask.objects.get(title="Gather information")
sub1.deadline = date.today() - timedelta(days=2)
sub1.save()

#8. Обновление — изменить описание SubTask 2
sub2 = SubTask.objects.get(title="Create slides")
sub2.description = "Create and format presentation slides"
sub2.save()

#9. Удаление Task и всех подзадач
task = Task.objects.get(title="Prepare presentation")
task.delete()