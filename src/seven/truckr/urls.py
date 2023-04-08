from django.contrib import admin
from django.urls import path, include


from . import views

#from here it goes to home and the other things will be accessed through buttons

urlpatterns = [
            #path('', views.index, name='index'),
            path('employees/', views.employees, name='employees'),
            path('shipmentsIn/', views.shipmentsIn, name='shipmentsIn'),
            path('shipmentsOut/', views.shipmentsOut, name='shipmentsOut'),
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
            ]
