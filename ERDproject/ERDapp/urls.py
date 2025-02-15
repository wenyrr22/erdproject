from django.contrib import admin
from django.urls import path, include
from .views import hello, all_task, today_tasks, task_added, add_task, edit_task, task_edited



urlpatterns = [
    path('', hello, name='hello'),
    path('all_task/', all_task, name='all_task'),
    path('today_tasks/', today_tasks, name='today_tasks'),
    path('task_added/', task_added, name="task_added"),
    path('add_task/<str:title>/', add_task, name='add_task'),
    path('edit_task/<str:title>/', edit_task, name='edit_task'),
    path('task_updated/<str:title>/', task_edited, name = 'task_update')
]
