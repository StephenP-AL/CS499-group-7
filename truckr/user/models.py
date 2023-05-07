# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    employeeid = models.AutoField(db_column='employeeID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    accounttype = models.CharField(db_column='accountType', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'


class Client(models.Model):
    clientid = models.AutoField(db_column='clientID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    clientname = models.CharField(db_column='clientName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Employee(models.Model):
    employeeid = models.AutoField(db_column='employeeID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mname = models.CharField(db_column='mName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='lName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=6, blank=True, null=True)
    homephone = models.CharField(db_column='homePhone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='cellPhone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay = models.TextField(blank=True, null=True)  # This field type is a guess.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Maintenance(models.Model):
    maintid = models.AutoField(db_column='maintID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    vehid = models.ForeignKey('Vehicle', models.SET_NULL, db_column='vehID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=30, blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)
    partslist = models.ForeignKey('Partslist', models.SET_NULL, db_column='partsList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maintenance'


class Manifest(models.Model):
    manifestid = models.AutoField(db_column='manifestID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    costshippinghandling = models.TextField(db_column='costShippingHandling', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'manifest'


class Manifestitem(models.Model):
    manifestid = models.OneToOneField(Manifest, models.SET_DEFAULT, db_column='manifestID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.SET_NULL, db_column='productID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifestItem'


class Orderitem(models.Model):
    purchaseorderid = models.OneToOneField('Purchaseorder', models.SET_DEFAULT, db_column='purchaseOrderID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.SET_NULL, db_column='productID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderItem'


class Part(models.Model):
    partid = models.AutoField(db_column='partID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    onhand = models.IntegerField(db_column='onHand', blank=True, null=True)  # Field name made lowercase.
    partname = models.CharField(db_column='partName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'part'


class Partslist(models.Model):
    listid = models.AutoField(db_column='listID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    partid = models.ForeignKey(Part, models.SET_NULL, db_column='partID', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=30, blank=True, null=True)
    cost = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'partsList'


class Product(models.Model):
    productid = models.AutoField(db_column='productID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    productname = models.CharField(db_column='productName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Purchaseorder(models.Model):
    purchaseorderid = models.AutoField(db_column='purchaseOrderID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    costshippinghandling = models.TextField(db_column='costShippingHandling', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'purchaseOrder'


class Shipmentin(models.Model):
    shipid = models.CharField(db_column='shipID', primary_key=True, max_length=10, blank=True, null=False)  # Field name made lowercase.
    clientid = models.ForeignKey(Client, models.SET_NULL, db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    vehid = models.ForeignKey('Vehicle', models.SET_NULL, db_column='vehID', blank=True, null=True)  # Field name made lowercase.
    departure = models.DateTimeField(blank=True, null=True)
    estarrival = models.DateTimeField(db_column='estArrival', blank=True, null=True)  # Field name made lowercase.
    arrived = models.BooleanField(blank=True, null=True)
    payment = models.BooleanField(blank=True, null=True)
    driver = models.ForeignKey(Employee, models.SET_NULL, db_column='driver', blank=True, null=True)
    purchaseorder = models.ForeignKey(Purchaseorder, models.SET_NULL, db_column='purchaseOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipmentIn'


class Shipmentout(models.Model):
    shipid = models.CharField(db_column='shipID', primary_key=True, max_length=10, blank=True, null=False)  # Field name made lowercase.
    clientid = models.ForeignKey(Client, models.SET_NULL, db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    vehid = models.ForeignKey('Vehicle', models.SET_NULL, db_column='vehID', blank=True, null=True)  # Field name made lowercase.
    departure = models.DateTimeField(blank=True, null=True)
    estarrival = models.DateTimeField(db_column='estArrival', blank=True, null=True)  # Field name made lowercase.
    arrived = models.BooleanField(blank=True, null=True)
    payment = models.BooleanField(blank=True, null=True)
    driver = models.ForeignKey(Employee, models.SET_NULL, db_column='driver', blank=True, null=True)
    manifest = models.ForeignKey(Manifest, models.SET_NULL, db_column='manifest', blank=True, null=True)
    purchaseorder = models.ForeignKey(Purchaseorder, models.SET_NULL, db_column='purchaseOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipmentOut'


class Vehicle(models.Model):
    vehid = models.AutoField(db_column='vehID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    make = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    vehtype = models.CharField(db_column='vehType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loadcapacity = models.IntegerField(db_column='loadCapacity', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(blank=True, null=True)
    partslist = models.ForeignKey(Partslist, models.SET_NULL, db_column='partsList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicle'
