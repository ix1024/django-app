from django.http import HttpResponse
from django.shortcuts import render
import json


def api(request):
    data = {"name": 'kingwell'}
    return HttpResponse(json.dumps(data))


def hello(request):
    request.encoding = 'utf-8'
    context = {}
    context['hello'] = 'Hello World!'
    for key in request.GET:
        print(key, request.GET[key])
    id = None
    name = None
    if 'id' in request.GET and request.GET['id']:
        id = request.GET['id']
    else:
        id = None
    context['id'] = id

    if 'name' in request.GET and request.GET['name']:
        id = request.GET['name']
    else:
        name = None
    context['name'] = name
    return render(request, 'hello.html', context)
