"""class_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('function_string/',function_string,name='function_string'),
    path('class_string/',class_string.as_view(),name='class_string'),

    path('function_html/',function_html,name='function_html'),
    path('class_html/',class_html.as_view(),name='class_html'),

    path('function_form/',function_form,name='function_form'),
    path('class_form/',class_form.as_view(),name='class_form'),

    path('form/',TemplateView.as_view(template_name='form.html'),name='form'),
]
