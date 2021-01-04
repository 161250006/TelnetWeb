from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('handle_command', views.handle_command, name='handle_command'),
]
