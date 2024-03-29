from django.contrib import admin
from .models import employee,product,orderItem,purchaseOrder,shipmentIn,shipmentOut,manifest,manifestItem,vehicle,part,partsList,maintenance,account


class adminEmployee(admin.ModelAdmin):
    list_display = ['username','lName','fName','mName']

#Customized title for admin site
admin.site.site_header = "Truckr Administration"

# Register your models here.

admin.site.register(employee,adminEmployee)
admin.site.register(product)
admin.site.register(orderItem)
admin.site.register(purchaseOrder)
admin.site.register(shipmentIn)
admin.site.register(shipmentOut)  
admin.site.register(manifest)
admin.site.register(manifestItem)  
admin.site.register(vehicle)
admin.site.register(part) 
admin.site.register(partsList)  
admin.site.register(maintenance)
admin.site.register(account)

#Template for copypasta
#admin.site.register(<++>)  
