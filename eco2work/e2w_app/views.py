from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from datetime import date

from .models import Activity
from .forms import RegisterForm, LoginForm


def index(request):
    activity_all = Activity.objects.all()
    days_list = [n for n in range(1, 31)]
    weeks_number = [n for n in range(5)]
    month_sum = 0

    today = date.today()

    for a in activity_all:
        month_sum += a.distance

    return render(request, 'index.html', {
        'activity_all': activity_all,
        'days_list': days_list,
        'today': today,
        'weeks_number': weeks_number,
        'month_sum': month_sum,
        })


def register_page(request):
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


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password= password)
        if user:
            login(request, username)
            return redirect('index')
        else:
            messages.error(request, 'Invalid input, please try again')
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)