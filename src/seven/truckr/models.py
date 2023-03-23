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

