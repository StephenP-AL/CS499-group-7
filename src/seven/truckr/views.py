from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from truckr.models import employee,product,purchaseOrder,orderItem


def index(request):
    return HttpResponse("Truckr Index")

def employees(request):
    elist = employee.objects.order_by('employeeID')
    context = {'elist': elist}
    return(render(request, 'truckr/employees.html', context))

def products(request):
    plist = product.objects.order_by('productID')
    context = {'plist': plist}
    return(render(request, 'truckr/products.html', context))

def purchaseOrders(request):
    polist  = purchaseOrder.objects.order_by('purchaseOrderID')
    context = {'polist':polist}
    return(render(request, 'truckr/purchaseOrders.html', context))

def purchaseOrderDetail(request, ID):
    # Join the orderitem table with the product table to display product data for that order. Filters for a specific purchase order
    items = orderItem.objects.raw('SELECT truckr_orderitem.id as id, truckr_orderitem.purchaseOrderID as purchaseOrderID, truckr_orderitem.productID as productID, truckr_product.productName as productName, truckr_product.price as price, truckr_orderitem.quantity as quantity, truckr_orderitem.status as status FROM truckr_orderitem INNER JOIN truckr_product ON truckr_orderitem.productID = truckr_product.productID WHERE truckr_orderitem.purchaseOrderID = %s', [ID])
#inferior code    items = orderItem.objects.filter(purchaseOrderID = ID)
    context = {'items':items}
    return(render(request, 'truckr/purchaseOrdersDetail2.html', context))

