from django.urls import path

from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('employee.html', views.employee, name='employee')
            ]
