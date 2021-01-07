from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('init_config', views.init_config, name='handle_command'),
    path('acl_config', views.acl_config, name='acl_config'),
    path('cancel_acl_config', views.cancel_acl_config, name='cancel_acl_config'),
    path('verify', views.verify, name='verify'),
]
