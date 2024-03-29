from django.db import models

# Create your models here.
class employee(models.Model):
    fName = models.CharField(max_length=30)
    mName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipCode = models.CharField(max_length=5)
    homePhone= models.CharField(max_length=10)
    cellPhone= models.CharField(max_length=10)
    pay = models.DecimalField(max_digits=10, decimal_places=2)
    startDate = models.DateTimeField('Start Date')
    employeeID = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.username

#Products to be shipped
class product(models.Model):
    productID = models.IntegerField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    productName = models.CharField(max_length=30)
    def __str__(self):
        return productName

#Aggregation of products in a purchase order
class orderItem(models.Model):
    purchaseOrderID = models.IntegerField()
    productID = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length = 11)

#Purchase Order
class purchaseOrder(models.Model):
    purchaseOrderID = models.IntegerField(primary_key = True)
    costShippingHandling = models.DecimalField(max_digits = 10, decimal_places = 2)

#Manifest
class manifest(models.Model):
    manifestID = models.IntegerField(primary_key = True)
    costShippingHandling = models.DecimalField(max_digits = 10, decimal_places = 2)

#Aggregation of products in a manifest
class manifestItem(models.Model):
    manifestID = models.IntegerField()
    productID = models.IntegerField()
    quantity = models.IntegerField()

#Inbound shipments
class shipmentIn(models.Model):
    shipID = models.CharField(max_length = 10, primary_key = True)
    #clientID = models.IntegerField()
    vehID = models.IntegerField()
    departure = models.DateTimeField()
    estArrival = models.DateTimeField()
    arrived = models.BooleanField()
    payment = models.BooleanField()
    driver = models.IntegerField()
    purchaseOrder = models.IntegerField()
    clientName = models.CharField(max_length = 20)
    street = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 6)

#Outgoing shipments
class shipmentOut(models.Model):
    shipID = models.CharField(max_length = 10, primary_key = True)
    #clientID = models.IntegerField()
    vehID = models.IntegerField()
    departure = models.DateTimeField()
    estArrival = models.DateTimeField()
    arrived = models.BooleanField()
    payment = models.BooleanField()
    driver = models.IntegerField()
    manifest = models.IntegerField()
    purchaseOrder = models.IntegerField()
    clientName = models.CharField(max_length = 20)
    street = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 6)

#Employee account types
class account(models.Model):
    employeeID = models.IntegerField(primary_key = True)
    accountType = models.CharField(max_length = 5)

#Vehicles
class vehicle(models.Model):
    vehID = models.IntegerField(primary_key = True)
    make = models.CharField(max_length  = 20)
    model = models.CharField(max_length = 20)
    year = models.IntegerField()
    vehType = models.CharField(max_length = 20)
    loadCapacity = models.IntegerField()
    height = models.IntegerField()
    partsList = models.IntegerField()

#Vehicle parts
class part(models.Model):
    partID = models.IntegerField(primary_key = True)
    onHand = models.IntegerField()
    partName = models.CharField(max_length = 30)

#lists of vehicle parts for vehicles and maintenance services
class partsList(models.Model):
    listID = models.IntegerField()
    partID = models.IntegerField()
    source = models.CharField(max_length = 30)
    cost = models.DecimalField(max_digits = 10, decimal_places = 2)

#Vehicle maintenance services
class maintenance(models.Model):
    maintID = models.IntegerField(primary_key = True)
    vehID = models.IntegerField()
    description = models.CharField(max_length = 30)
    completed = models.DateTimeField()
    partsList = models.IntegerField()

#Available hyperlinks based on account types
class navbar(models.Model):
    accountType = models.CharField(max_length = 5)
    text = models.CharField(max_length = 30)
    url = models.CharField(max_length = 40)

#Dates for selecting reports
class yearmonth(models.Model):
    year = models.CharField(max_length = 4)
    month = models.CharField(max_length = 2)
    period = models.CharField(max_length = 6, primary_key = True)
