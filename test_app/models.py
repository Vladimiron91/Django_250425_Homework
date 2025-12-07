from typing import Any

from django.db import models
from django.core.validators import MinLengthValidator

#MODEL: Book
class Book(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание книги")
    author = models.CharField(max_length=100, verbose_name="Название автора")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")

    def __str__(self):
        return f"Book '{self.title}' -- Author '{self.author}'"

    class Meta:
        db_table = "books"
        ordering = ["published_date"]
        verbose_name = "Book"
        verbose_name_plural = "Books"
        get_latest_by = "published_date"
        unique_together = ["title", "published_date"]
        indexes = [
            models.Index(
                fields=["title", "published_date"],
                name="idx_book_title_pub_date",
            )
        ]

#MODEL: Post
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    nickname = models.CharField(max_length=70, unique=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    followers_count = models.PositiveBigIntegerField(null=True, blank=True)
    posts_count = models.PositiveSmallIntegerField(null=True, blank=True) # 0 -> 32672
    post_comments = models.PositiveSmallIntegerField(null=True, blank=True)
    engagement_rate = models.FloatField(null=True, blank=True) # 99.99

    def __str__(self):
        return self.nickname

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
    deadline = models.DateTimeField(null=True, blank=True)
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

from typing import Any

from django.db import models
from django.core.validators import MinLengthValidator


# MODEL: Book
class Book(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание книги")
    author = models.CharField(max_length=100, verbose_name="Название автора")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    pages = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Book '{self.title}' -- Author '{self.author}'"

    class Meta:
        db_table = "books"
        ordering = ["published_date"]
        verbose_name = "Book"
        verbose_name_plural = "Books"
        get_latest_by = "published_date"
        unique_together = ["title", "published_date"]

        indexes = [
            models.Index(
                fields=["title", "published_date"],
                name="idx_book_title_pub_date",
            )
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["title", "published_date"],
                name="unq_title_pub_date",
            ),
            models.CheckConstraint(
                check=models.Q(pages__gte=0),
                name="book_pages_constraint",
            ),
        ]


# MODEL: Post
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    nickname = models.CharField(max_length=70, unique=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    followers_count = models.PositiveBigIntegerField(null=True, blank=True)
    posts_count = models.PositiveSmallIntegerField(null=True, blank=True)  # 0 -> 32672
    post_comments = models.PositiveSmallIntegerField(null=True, blank=True)
    engagement_rate = models.FloatField(null=True, blank=True)  # 99.99

    def __str__(self):
        return self.nickname


# MODEL: Category
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
                name="unique_category_name",
            )
        ]


# MODEL: Task
class Task(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        validators=[MinLengthValidator(10)],
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
        default="New",
    )

    priority = models.CharField(
        max_length=20,
        choices=[
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
            ("Very High", "Very High"),
        ],
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["title"],
                name="unique_task_title",
            )
        ]

'''Модель SubTask:
Добавить метод str, который возвращает название подзадачи.
Добавить класс Meta с настройками:
Имя таблицы в базе данных: 'task_manager_subtask'.
Сортировка по убыванию даты создания.
Человекочитаемое имя модели: 'SubTask'.
Уникальность по полю 'title'.'''

# MODEL: SubTask
class SubTask(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
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
        default="New",
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
                name="unique_subtask_title",
            )
        ]

    class Test(models.Model):
        ...