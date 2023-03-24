from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from truckr.models import employee,product,purchaseOrder


def index(request):
    return HttpResponse("Truckr Index")

def employees(request):
    elist = employee.objects.order_by('employeeID')
    context = {'elist': elist}
    return(render(request, 'truckr/employees.html', context))
    return HttpResponse("Employee page")

def products(request):
    plist = product.objects.order_by('productID')
    context = {'plist': plist}
    return(render(request, 'truckr/products.html', context))
    return HttpResponse("Product page")

def purchaseOrders(request):
    polist  = purchaseOrder.objects.order_by('purchaseOrderID')
    context = {'polist':polist}
    return(render(request, 'truckr/purchaseOrders.html', context))
    return HttpResponse("Purchase orders")

def purchaseOrderDetail(request, purchaseOrderID):
    return HttpResponse("Viewing Purchase Order %s" % purchaseOrderID)

