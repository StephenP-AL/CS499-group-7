from django.contrib import admin
from .models import employee,product,orderItem,purchaseOrder,shipmentIn,shipmentOut,manifest,manifestItem

class adminEmployee(admin.ModelAdmin):
    list_display = ['username','lName','fName','mName']

# Register your models here.

admin.site.register(employee,adminEmployee)
admin.site.register(product)
admin.site.register(orderItem)
admin.site.register(purchaseOrder)
admin.site.register(shipmentIn)
admin.site.register(shipmentOut)  
admin.site.register(manifest)
admin.site.register(manifestItem)  
#Template for copypasta
#admin.site.register(<++>)  
