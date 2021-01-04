from django.shortcuts import render
from django.http import HttpResponse
from . import service


def index(request):
    service.connect()
    return render(request, 'index.html')


def handle_command(request):
    request.encoding = 'UTF-8'
    if request.method == 'GET':
        command = request.GET.get('command')
        routing = request.GET.get('routing')
        return HttpResponse(service.send_command(command, routing))
