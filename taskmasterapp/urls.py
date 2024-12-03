from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    path('registro/', views.registro_view, name='registro'),

    path('taskregister/', views.registrotarefas_view, name='tasksregister'),

    path('tarefas/', views.TaskList_view, name='task'),
]
