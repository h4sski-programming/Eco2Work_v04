from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from datetime import date, timedelta

from .models import Activity
from .forms import RegisterForm, LoginForm


@login_required(login_url='login_view')
def index(request):
    today = date.today()
    month_first_day = today.replace(day=1)
    month_last_day = today.replace(month=today.month + 1, day=1) - timedelta(days=1)

    days_list = [n for n in range(month_first_day.day, month_last_day.day + 1)]

    activity_all = Activity.objects.all()
    users_all = User.objects.all()

    month_sum = {}
    for u in users_all:
        user_sum = 0
        for a in activity_all:
            if a.user == u:
                user_sum += a.distance
        month_sum[u] = user_sum

    context = {
        'activity_all': activity_all,
        'users_all': users_all,
        'days_list': days_list,
        'today': today,
        'month_sum': month_sum,
        }
    return render(request, 'index.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid input, try again')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Hello {user}, you are logged in. Enjoy!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid input, please try again')
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login_view')
