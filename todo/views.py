from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm, UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
        return render(request, 'home.html', {"todos": todos})
    else:
        return render(request, 'home.html')


# Register New user
def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)

            return redirect('home')

    else:
        form = UserRegistrationForm()

    return render(request, 'auth/register.html', {"form": form})


@login_required
# Add New Todo
def store(request):
    if request.method == "POST":
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.status = 1
            user.user = request.user
            user.save()

            if request.POST.get('action') == 'save_last':
                return redirect('home')
            else:
                return redirect('store')
    else:
        form = TodoForm()

    return render(request, 'add-todo.html', {"form": form})
