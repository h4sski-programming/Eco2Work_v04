from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

from .models import Activity
from .forms import RegisterForm, LoginForm


@login_required(login_url='login_view')
def index(request):
    today = date.today()
    month_first_day = today.replace(day=1)
    month_last_day = month_first_day + relativedelta(months=+1) - timedelta(days=1)

    days_list = [n for n in range(month_first_day.day, month_last_day.day + 1)]

    # activity_all = Activity.objects.all()
    activity_all = Activity.objects.filter(date__month=today.month)
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


@login_required(login_url='login_view')
def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    today = date.today()
    
    user_active = request.user
    user_activities = Activity.objects.filter(user=user_active).order_by('date')
    u = Activity.objects.filter(user=user_active)
    print(u)
    
    testing_list = ['user', 'bike', 23, 'abcd']
    testing_dictionary = {
        'name': 'myself',
        'vehicle': 'bike',
        'sum': 14,
        'abcd': 'DCBA',
        'key': 'value',
    }
    
    context = {
        'today': today,
        'user_active': user_active,
        'user_activities': user_activities,
        'u': u,
        'testing_dictionary': testing_dictionary,
        'testing_list': testing_list,
    }
    return render(request, 'profile.html', context)



@login_required(login_url='login_view')
def show_view(request, year, month):
    if not request.user.is_authenticated:
        return redirect('index')
    
    today = date.today()
    if year > today.year or \
        (year == today.year and month > today.month):
        messages.error(request, f'Incorrect year, cant look into future. Today is {today}.')
        return redirect('index')
    
    year_m1 = year - 1
    year_p1 = year + 1
    month_m1 = month - 1
    month_p1 = month + 1
    if month == 1:
        month_m1 = 12
    elif month == 12:
        month_p1 = 1
    
    date_start = date(year=year, month=month, day=1)
    date_end = date_start + relativedelta(months=+1) - timedelta(days=1)
    month_number_of_days = [x+1 for x in range(date_end.day)]
    
    activities_all_filtered = Activity.objects.filter(date__year=year, date__month=month)
    
    users = {a.user for a in activities_all_filtered}
    activities = {a.user: [] for a in activities_all_filtered}
    for a in activities_all_filtered:
        activities[a.user].append([a.date.day, a.distance])
    # print(activities)
    
    context = {
        'year': year,
        'month': month,
        'year_m1': year_m1,
        'year_p1': year_p1,
        'month_m1': month_m1,
        'month_p1': month_p1,
        'date_start': date_start,
        'date_end': date_end,
        'month_number_of_days': month_number_of_days,
        'activities': activities,
        'users': users,
    }
    return render(request, 'show.html', context)


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