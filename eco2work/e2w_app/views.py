from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from datetime import date

from .models import Activity
from .forms import RegisterForm, LoginForm


@login_required(login_url='login_view')
def index(request):
    activity_all = Activity.objects.all()
    users_all = User.objects.all()
    days_list = [n for n in range(1, 31)]
    month_sum = 0

    today = date.today()

    for a in activity_all:
        month_sum += a.distance

    def fill_activities_to_display():
        #   {'user':[[a1, a2, a3, a4], sum]
        output = {}
        for u in users_all:
            output[u.username] = [[], 0]

        for a in activity_all:
            output[a.user.username][0].append(a)

        for u in output:
            u_sum = 0
            for act in output[u][0]:
                u_sum += act.distance
                print(act)
            output[u][1] = u_sum

        return output

    # fill_activities_to_display()
    activities_to_display = fill_activities_to_display()

    test_dic = [
            ['user1', [1, 2, 34, 5, 67, 6], 5],
            ['user2', [5, 3, 8, 6, 3, 23, 3], 50],
        ]

    context = {
        'activity_all': activity_all,
        'activities_to_display': activities_to_display,
        'test_dic': test_dic,
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
