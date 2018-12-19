from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.get_many_tasks, name='get_tasks'),
    path('tasks/<int:task_id>', views.get_one_task, name='get_task'),
]

