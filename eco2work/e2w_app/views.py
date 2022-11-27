from django.shortcuts import render
from django.http import HttpResponse        # to be removed later


def index(request):
    return HttpResponse('Hello from e2w_app, page index.')
