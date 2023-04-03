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
    homePhone= models.CharField(max_length=5)
    cellPhone= models.CharField(max_length=5)
    pay = models.DecimalField(max_digits=10, decimal_places=2)
    startDate = models.DateTimeField('Start Date')
    employeeID = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.username

class product(models.Model):
    productID = models.IntegerField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    productName = models.CharField(max_length=30)
    def __str__(self):
        return productName

class orderItem(models.Model):
    purchaseOrderID = models.IntegerField()
    productID = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length = 11)

class purchaseOrder(models.Model):
    purchaseOrderID = models.IntegerField(primary_key = True)
    costShippingHandling = models.DecimalField(max_digits = 10, decimal_places = 2)

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

class account(models.Model):
    employeeID = models.IntegerField(primary_key = True)
    accountType = models.CharField(max_length = 5)
