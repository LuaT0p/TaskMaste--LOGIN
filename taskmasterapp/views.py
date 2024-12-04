from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm

def login_view(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('taskregister/')
        else:
            return render(request, 'login/index.html', {'error': 'Credenciais invalidas'})
    
    
    return render(request, 'login/index.html')

def registro_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("registro")
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Usuário registrado com sucesso! Faça login.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Erro ao registrar usuário: {e}")
            return redirect("registro")
    return render(request, 'registro/Cadastrar.html')

def registrotarefas_view(request):
    if request.method == "POST":
        # Obtém os dados do formulário
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority")

        # Cria a tarefa e associa ao usuário logado
        Task.objects.create(
            user=request.user,  # Associando ao usuário logado
            title=title,
            due_date=due_date,
            priority=priority,
        )
        
        return redirect("task")
    return render(request, "taskregister/taskregister.html")

def TaskList_view(request):
    tasks = Task.objects.filter(user=request.user)  # Filtra tarefas do usuário logado
    return render(request, "task/task.html", {"tasks": tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = TaskForm(instance=task)
        return render(request, 'taskedit/index.html', {'form': form, 'task': task})