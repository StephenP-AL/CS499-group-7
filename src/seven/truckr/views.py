from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import employee


def index(request):
    return HttpResponse("Truckr Index")

def employee(request):
    elist = employee.objects.order_by('employeeID')
    cotext = {'elist': elist}
    return(render(request, 'truckr/employee.html', context))

#    return HttpResponse("Employee page")
