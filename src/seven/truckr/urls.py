from django.urls import path

from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('employees/', views.employees, name='employees'),
            path('products/', views.products, name = 'products'),
            path('purchaseOrders/', views.purchaseOrders, name = 'purchaseOrders'),
            path('purchaseOrders/<int:purchaseOrderID>/', views.purchaseOrderDetail, name='purchaseOrderDetail'),
            ]
