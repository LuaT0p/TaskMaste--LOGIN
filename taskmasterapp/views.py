from django.shortcuts import render

def login_view(request):
    return render(request, 'login/index.html')

def TaskList_view(request):
    return render(request, 'TaskList/tasks.html')