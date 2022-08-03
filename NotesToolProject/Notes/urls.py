from django.contrib import admin
from django.urls import path

from .views import home_view, delete_post, mark_task, edit_task, edit_task_post

urlpatterns = [
    path('notes/', home_view, name = 'homeget'),
    path('notes/delete/<int:id>/', delete_post, name = 'delete_task'),
    path('notes/mark/<int:id>/', mark_task, name = 'mark_task'),
    path('notes/edit/<int:id>/', edit_task, name = 'edit_task'),
    path('notes/redit/<int:id>/', edit_task_post, name = 'edit_post_task'),
]