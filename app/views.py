from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . models import Task, Category
from . forms import TaskForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    context = {"form":form}
    return render(request, 'login.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print()
        if form.is_valid():
            user =  form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    context = {"form":form}
    return render(request, 'signup.html', context)

@login_required
def dashboard(request):
    current_user = request.user
    records = Task.objects.filter(user=current_user.id)
    context = {"tasks": records}
    return render(request, 'dashboard.html', context)


@login_required
def create_task(request):
    if request.method == 'POST':
        instance = Task(
            title = request.POST['title'],
            description = request.POST['description'],
            category = Category.objects.get(pk=request.POST['category']),
            user = request.user,
            start_datetime = request.POST['start_datetime'],
            end_datetime = request.POST['end_datetime']
        )
        instance.save()
        return redirect('dashboard')
    else:
        form = TaskForm()
    context = {"form":form}
    return render(request, 'create_task.html', context)