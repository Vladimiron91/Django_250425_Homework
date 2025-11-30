# Register your models here.
from django.contrib import admin,messages

from test_app.models import Book, Task, SubTask, Category, Post, UserProfile

"""Задание 1: Добавить настройку инлайн форм для админ класса задач. 
При создании задачи должна появиться возможность создавать сразу и подзадачу."""

#INLINE SubTask, чтобы создавать подзадачи внутри Task

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1 # количество пустых форм при создании задачи
    fields = ['title', 'description', 'status', 'deadline']

"""Названия задач могут быть длинными и ухудшать читаемость в Админ панели, поэтому требуется выводить в 
списке задач укороченный вариант – первые 10 символов с добавлением «...», если название длиннее, 
при этом при выборе задачи для создания подзадачи должно отображаться полное название. Необходимо реализовать 
такую возможность."""

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "priority", "created_at")
    list_filter = ("status", "priority")
    search_fields = ("title", "description")
    readonly_fields = ['created_at']

    inlines = [SubTaskInline]

    @admin.display(description="Название")
    def abb_title(self, obj):
        return f"{obj.title[:10]}..." if len(obj.title) > 10 else obj.title

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'task', 'status', 'deadline', 'created_at']
    list_filter = ['status', 'created_at']
    raw_id_fields = ['task']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    actions = ['mark_selected_as_done']



'''Реализовать свой action для Подзадач, который поможет выводить выбранные 
Админ панели объекты в статус Done'''

@admin.action(description='Mark selected subtasks as Done')
def mark_selected_as_done(self, request, queryset):
    updated = queryset.exclude(status='Done').update(status='Done')
    self.message_user(
        request,
        f'{updated} subtasks marked as Done',
        messages.SUCCESS
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Book)
admin.site.register(Post)
admin.site.register(UserProfile)


