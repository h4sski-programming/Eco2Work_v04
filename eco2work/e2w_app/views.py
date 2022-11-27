from django.shortcuts import render

from .models import Activity


def index(request):
    activity_all = Activity.objects.all()
    days_list = [n for n in range(1, 31)]
    weeks_number = [n for n in range(5)]
    month_sum = 0
    for a in activity_all:
        month_sum += a.distance

    return render(request, 'index.html', {
        'activity_all': activity_all,
        'days_list': days_list,
        'weeks_number': weeks_number,
        'month_sum': month_sum,
        })
