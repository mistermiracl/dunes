from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.


def index(request):
    sql = '%s\\config\\schema.sql' % settings.PROJECT_ROOT #ESCAPE THE BACKSLASH TO PREVENT WARNING FROM LINTER
    with open(sql, 'r') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]
        [print(line) for line in lines]
    return HttpResponse("<h1>Getting started</h1>")