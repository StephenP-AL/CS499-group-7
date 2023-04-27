from django.contrib import admin
from django.urls import path, include


from . import views

#from here it goes to home and the other things will be accessed through buttons

urlpatterns = [
            #path('', views.index, name='index'),
            path('employees', views.employees, name='employees'),
            path('shipmentsIn', views.shipmentsIn, name='shipmentsIn'),
            path('shipmentsOut', views.shipmentsOut, name='shipmentsOut'),
            path('products/', views.products, name = 'products'),
            path('purchaseOrders/', views.purchaseOrders, name = 'purchaseOrders'),
            path('purchaseOrders/<int:ID>/', views.purchaseOrderDetail, name='purchaseOrderDetail'),
            path('', views.home, name="home"),
            path('signup', views.signup, name="signup"),
            path('signin', views.signin, name="signin"),
            path('signout', views.signout, name="signout"),
            path('admin/', admin.site.urls),
            path('manifestDetail/<int:ID>/', views.manifestDetail, name='manifestDetail'),
            path('manageShipmentsIn', views.manageShipmentsIn, name = 'manageShipmentsIn'),
            path('manageShipmentsOut', views.manageShipmentsOut, name = 'manageShipmentsOut'),
            path('vehicles', views.vehicles, name = 'vehicles'),
            path('vehiclesDetail/<int:ID>/', views.vehiclesDetail, name = 'vehiclesDetail'),
            path('maintenance', views.maintenanceview, name = 'maintenance'),
            path('maintenanceDetail/<int:ID>/', views.maintenanceDetail, name = 'maintenanceDetail'),
            path('maintenanceReport/', views.maintenanceReportList, name = 'maintenanceReportList'),
            path('maintenanceReport/<int:year>/<int:month>/', views.maintenanceReport, name = 'maintenanceReport'),
            path('vehicleReport/<int:ID>/', views.vehicleReport, name = 'vehicleReport'),
            path('payReport/<int:year>/<int:month>/',views.payReport, name = 'payReport'),
            path('payReport/',views.payReportList, name = 'payReportList'),
            path('shipReport/<int:year>/<int:month>/',views.shipReport, name = 'shipReport'),
            path('shipReport/', views.shipReportList, name = 'shipReportList')
            ]
