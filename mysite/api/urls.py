from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('tasks/<int:task_id>', views.get_task, name='get_task'),
]

