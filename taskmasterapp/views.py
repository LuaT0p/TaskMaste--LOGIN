from django.shortcuts import render

def login_view(request):
    return render(request, 'login/index.html')

def TaskList_view(request):
    return render(request, 'TaskList/tasks.html')

def registro_view(request):
    return render(request, 'registro/Cadastrar.html')

def registrotarefas_view(request):
    return render(request, 'registrotarefas/registrotarefas.html')