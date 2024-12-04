from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    path('registro/', views.registro_view, name='registro'),

    path('taskregister/', views.registrotarefas_view, name='tasksregister'),

    path('tarefas/', views.TaskList_view, name='task'),

    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),

    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
