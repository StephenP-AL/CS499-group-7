from django.urls import path

from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('employees.html', views.employees, name='employees')
            ]
