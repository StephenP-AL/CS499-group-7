from django.contrib import admin
from .models import employee,product,orderItem,purchaseOrder,shipmentIn,shipmentOut

# Register your models here.

admin.site.register(employee)
admin.site.register(product)
admin.site.register(orderItem)
admin.site.register(purchaseOrder)
admin.site.register(shipmentIn)
admin.site.register(shipmentOut)  

#Template for copypasta
#admin.site.register(<++>)  
