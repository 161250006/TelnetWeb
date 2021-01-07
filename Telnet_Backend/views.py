from django.shortcuts import render
from django.http import HttpResponse
from . import service


def index(request):
    service.connect()
    return render(request, 'index.html')


# 初始化配置：路由器的hostname，ip地址和子网掩码
def init_config(request):
    request.encoding = 'UTF-8'
    if request.method == 'GET':
        routing = request.GET.get('routing')
        hostname = request.GET.get('hostname')
        ip_address = request.GET.get('ip_address')
        mask = request.GET.get('mask')

        return HttpResponse(service.init_config(routing, hostname, ip_address, mask))


# 自动化配置acl
def acl_config(request):
    request.encoding = 'UTF-8'
    if request.method == 'GET':
        routing = request.GET.get('routing')

        return HttpResponse(service.acl_config(routing))


# 清空acl配置
def cancel_acl_config(request):
    request.encoding = 'UTF-8'
    if request.method == 'GET':
        routing = request.GET.get('routing')

        return HttpResponse(service.cancel_acl_config(routing))


# 验证是否配置成功
def verify(request):
    request.encoding = 'UTF-8'
    if request.method == 'GET':
        routing = request.GET.get('routing')

        return HttpResponse(service.verify(routing))
