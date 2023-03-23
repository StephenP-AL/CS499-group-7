from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from truckr.models import employee


def index(request):
    return HttpResponse("Truckr Index")

def employees(request):
    elist = employee.objects.order_by('employeeID')
    context = {'elist': elist}
    return(render(request, 'truckr/employees.html', context))
    return HttpResponse("Employee page")
