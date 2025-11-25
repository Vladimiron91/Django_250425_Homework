from django.db import models
from django.core.validators import MinLengthValidator

#MODEL: Book
class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField()

'''Модель Category:
Добавить метод str, который возвращает название категории.
Добавить класс Meta с настройками:
Имя таблицы в базе данных: 'task_manager_category'.
Человекочитаемое имя модели: 'Category'.
Уникальность по полю 'name'.'''

#MODEL: Category
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "task_manager_category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_category_name"
            )
        ]

'''Домашнее задание: Проект "Менеджер задач" — продолжение
Цель:
Добавить строковое представление (str) и метаданные (Meta) к моделям менеджера задач, а также настроить административную панель для удобного управления этими моделями.
Реализуйте изменения в моделях:
Модель Task:
Добавить метод str, который возвращает название задачи.
Добавить класс Meta с настройками:
Имя таблицы в базе данных: 'task_manager_task'.
Сортировка по убыванию даты создания.
Человекочитаемое имя модели: 'Task'.
Уникальность по полю 'title'.'''

#MODEL: Task
class Task(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        validators=[MinLengthValidator(10)]
    )
    description = models.TextField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ("New", "New"),
            ("In_progress", "In Progress"),
            ("Completed", "Completed"),
            ("Closed", "Closed"),
            ("Pending", "Pending"),
            ("Blocked", "Blocked"),
        ],
        default="New"
    )

    priority = models.CharField(
        max_length=20,
        choices=[
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
            ("Very High", "Very High"),
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-created_at"]  # сортировка
        constraints = [
            models.UniqueConstraint(
                fields=["title"],
                name="unique_task_title"
            )
        ]

'''Модель SubTask:
Добавить метод str, который возвращает название подзадачи.
Добавить класс Meta с настройками:
Имя таблицы в базе данных: 'task_manager_subtask'.
Сортировка по убыванию даты создания.
Человекочитаемое имя модели: 'SubTask'.
Уникальность по полю 'title'.'''

#MODEL: SubTask
class SubTask(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=[
            ("New", "New"),
            ("In_progress", "In Progress"),
            ("Completed", "Completed"),
            ("Closed", "Closed"),
            ("Pending", "Pending"),
            ("Blocked", "Blocked"),
        ],
        default="New"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_subtask"
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["title"],
                name="unique_subtask_title"
            )
        ]
