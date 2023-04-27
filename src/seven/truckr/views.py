from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from truckr.models import employee,product,purchaseOrder,orderItem,shipmentIn, shipmentOut,navbar,manifest,manifestItem,vehicle,part,partsList,maintenance,yearmonth


# Create your views here.

# Set of links based on user group
def navigation(username):
    nav = navbar.objects.raw(""" SELECT * FROM truckr_employee JOIN truckr_account ON truckr_employee.employeeID = truckr_account.employeeID JOIN truckr_navbar ON truckr_account.accountType = truckr_navbar.accountType WHERE truckr_employee.username = '%s' ORDER BY id; """ % username)
    return nav
#showes stuff to the webpage that the user can see


def home(request):
    username = request.user.username
    nav = navbar.objects.raw("""
                SELECT * FROM truckr_employee 
                JOIN truckr_account ON truckr_employee.employeeID = truckr_account.employeeID 
                JOIN truckr_navbar ON truckr_account.accountType = truckr_navbar.accountType
                WHERE truckr_employee.username = '%s'
                ORDER BY id;
            """ % username)
    return render(request, "truckr/index.html", {'nav': nav})
    #return render(request, "truckr/index.html")

def signup(request):
    #if we came here after pressing signup button, we get all the data from the form
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #creates a userwith that info
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your Account has been sucessfully created.")

        #redirect to loginpg
        return redirect('signin')

    return render(request, "truckr/signup.html")


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        #if user exists, log them in, if not print error message and take back to home
        if user is not None:
            login(request, user)
            nav = navigation(username)
            fname = user.first_name
            return render(request, "truckr/index.html", {'nav': nav,'fname':fname})
        
        else:
            messages.error(request, "Invalid Username add/or Password")
            return redirect('home')

    return render(request, "truckr/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def index(request):
    return HttpResponse("Truckr Index")

#employees page
def employees(request):
    username = request.user.username
    nav = navigation(username)
    #List of employee records
    elist = employee.objects.order_by('employeeID')
    # Single record if user is in full group. Used to hide employee data from non-full account users
    filt = employee.objects.raw("SELECT truckr_account.employeeID,username,accountType FROM truckr_employee JOIN truckr_account ON truckr_employee.employeeID = truckr_account.employeeID WHERE accountType = 'full' and username = '{}';".format(username))
    context = {'elist': elist, 'nav': nav,'filt':filt}
    return render(request, 'truckr/employees.html', context)

#Products listing page 
def products(request):
    username = request.user.username
    nav = navigation(username)

    plist = product.objects.order_by('productID')
    context = {'plist': plist,'nav': nav}
    return render(request, 'truckr/products.html', context)

#Purchase Orders list page
def purchaseOrders(request):
    username = request.user.username
    nav = navigation(username)

    polist  = purchaseOrder.objects.order_by('purchaseOrderID')
    context = {'polist':polist,'nav': nav}
    return(render(request, 'truckr/purchaseOrders.html', context))

# Details of individual purchase order
def purchaseOrderDetail(request, ID):
    username = request.user.username
    nav = navigation(username)
    po = purchaseOrder.objects.raw('SELECT * FROM truckr_purchaseorder WHERE purchaseOrderID = %s;',[ID])

    # Join the orderitem table with the product table to display product data for that order. Filters for a specific purchase order
    items = orderItem.objects.raw('SELECT truckr_orderitem.id as id, truckr_orderitem.purchaseOrderID as purchaseOrderID, truckr_orderitem.productID as productID, truckr_product.productName as productName, truckr_product.price as price, truckr_orderitem.quantity as quantity, truckr_orderitem.status as status FROM truckr_orderitem INNER JOIN truckr_product ON truckr_orderitem.productID = truckr_product.productID WHERE truckr_orderitem.purchaseOrderID = %s', [ID])

    context = {'items':items,'nav':nav, 'po':po}
    return(render(request, 'truckr/purchaseOrdersDetail2.html', context))

#Details of a shipment manifist
def manifestDetail(request,ID):
    username = request.user.username
    nav = navigation(username)
    man = manifest.objects.raw('SELECT * FROM truckr_manifest WHERE manifestID = %s;', [ID])
    items = manifestItem.objects.raw('SELECT id, truckr_manifestitem.manifestID as manifestID, truckr_manifestitem.productID as productID,truckr_manifestitem.quantity as quantity, truckr_product.price as price, truckr_product.productName as productName, ROUND(truckr_product.price * truckr_manifestitem.quantity,2) as total FROM truckr_manifestitem JOIN truckr_product ON truckr_manifestitem.productID = truckr_product.productID WHERE manifestID = %s;', [ID])
    context = {'nav':nav,'man':man, 'items':items}
    return(render(request,'truckr/manifestDetail.html', context))


#Driver views
def shipmentsIn(request):
    username = request.user.username
    nav = navigation(username)

    lst = shipmentIn.objects.raw("SELECT * from truckr_shipmentin JOIN truckr_employee ON truckr_shipmentin.driver = truckr_employee.employeeID WHERE truckr_employee.username = '%s';" % username)
    context = {'lst':lst,'nav': nav}
    return(render(request, 'truckr/shipmentsIn.html', context))

def shipmentsOut(request):
    username = request.user.username
    nav = navigation(username)
    lst = shipmentOut.objects.raw("SELECT * from truckr_shipmentout JOIN truckr_employee ON truckr_shipmentout.driver = truckr_employee.employeeID WHERE truckr_employee.username = '%s';" % username)
    context = {'lst':lst,'nav': nav}
    return(render(request, 'truckr/shipmentsOut.html', context))

#Shipping manager views
def manageShipmentsIn(request):
    username = request.user.username
    nav = navigation(username)

    lst = shipmentIn.objects.raw("SELECT * from truckr_shipmentin JOIN truckr_employee ON truckr_shipmentin.driver = truckr_employee.employeeID;")
    context = {'lst':lst,'nav': nav}
    return(render(request, 'truckr/manageShipmentsIn.html', context))

def manageShipmentsOut(request):
    username = request.user.username
    nav = navigation(username)

    lst = shipmentIn.objects.raw("SELECT * from truckr_shipmentout JOIN truckr_employee ON truckr_shipmentout.driver = truckr_employee.employeeID;")

    context = {'lst':lst,'nav': nav}
    return(render(request, 'truckr/manageShipmentsOut.html', context))

#Maintenance views
def vehicles(request):
    username = request.user.username
    nav = navigation(username)
    lst = vehicle.objects.raw("SELECT * FROM truckr_vehicle;")

    context = {'lst':lst,'nav': nav}
    return(render(request, 'truckr/vehicles.html', context))

def vehiclesDetail(request, ID):
    username = request.user.username
    nav = navigation(username)
    veh = vehicle.objects.raw("SELECT * FROM truckr_vehicle WHERE vehID = %s;", [ID] )
    parts = vehicle.objects.raw("SELECT * FROM truckr_vehicle JOIN truckr_partslist ON truckr_vehicle.partsList = truckr_partslist.listID JOIN truckr_part ON truckr_partslist.partID = truckr_part.partID WHERE truckr_vehicle.vehID = %s;", [ID])
    maint = maintenance.objects.raw("SELECT * FROM truckr_maintenance WHERE vehID = %s;",[ID] )
    context = {'veh': veh, 'nav': nav, 'parts':parts, 'maint':maint,}
    return(render(request, 'truckr/vehiclesDetail.html', context))

def maintenanceview(request):
    username = request.user.username
    nav = navigation(username)
    lst = maintenance.objects.raw("SELECT * FROM truckr_maintenance;")

    context = {'lst':lst,'nav': nav}
    return(render(request, 'truckr/maintenance.html', context))


def maintenanceDetail(request, ID):
    username = request.user.username
    nav = navigation(username)
    maint = maintenance.objects.raw("SELECT * FROM truckr_maintenance JOIN truckr_vehicle ON truckr_maintenance.vehID = truckr_vehicle.vehID WHERE truckr_maintenance.maintID = %s;", [ID])
    parts = maintenance.objects.raw("SELECT * FROM truckr_maintenance JOIN truckr_partslist ON truckr_maintenance.partsList = truckr_partslist.listID JOIN truckr_part ON truckr_partslist.partID = truckr_part.partID WHERE truckr_maintenance.maintID = %s;", [ID])
    context = {'nav':nav,'maint':maint, 'parts':parts}
    return(render(request, 'truckr/maintenanceDetail.html', context))

#Reports

#maintenance report for a single month
def maintenanceReport(request, year, month):
    username = request.user.username
    nav = navigation(username)
    yr = str(year)
    mo = str('{:02d}'.format(month))
    
    maint = maintenance.objects.raw("SELECT * FROM maintenance_rpt_bymonth WHERE yr = '{}' and mo = '{}';".format(yr,mo))
    context = {'nav':nav,'maint':maint}
    return(render(request, 'truckr/maintenanceReport.html', context))

#listing of all maintenance reports
def maintenanceReportList(request):
    username = request.user.username
    nav = navigation(username)
    
    maint = maintenance.objects.raw("SELECT * FROM maintenance_rpt_list;")
    context = {'nav':nav,'maint':maint}
    return(render(request, 'truckr/maintenanceReportList.html', context))

#listing of all maintenance performed on a vehicle
def vehicleReport(request, ID):
    username = request.user.username
    nav = navigation(username)
    veh = vehicle.objects.raw("SELECT * FROM truckr_vehicle WHERE vehID = %s;", [ID]) 
    maint = maintenance.objects.raw("SELECT * FROM maintenance_rpt_bymonth WHERE vehID = %s;", [ID])
    context = {'nav':nav,'maint':maint,'veh':veh,'ID':ID}
    return(render(request,'truckr/vehicleReport.html',context))
 
#monthly pay report
def payReport(request, year, month):
    username = request.user.username
    nav = navigation(username)
    #Formats year/month to a single field to use as a filter    
    period = str(year) + str('{:02d}'.format(month)) 

    #Calculates total monthly salary for all employees
    total = employee.objects.raw("SELECT truckr_account.employeeID, sum(pay) as total FROM payReport JOIN truckr_account ON payReport.ID = truckr_account.employeeID WHERE (yr||mo) <= '{}';".format(period))
    #List of all emplyees and salaries
    elst = employee.objects.raw("SELECT * FROM payReport JOIN truckr_account ON payReport.ID = truckr_account.employeeID WHERE (yr||mo) <= '{}';".format(period))
    #Used to restrict page to only full account
    filt = employee.objects.raw("SELECT truckr_account.employeeID,username,accountType FROM truckr_employee JOIN truckr_account ON truckr_employee.employeeID = truckr_account.employeeID WHERE accountType = 'full' and username = '{}';".format(username))
    context = {'nav':nav, 'total':total,'filt':filt,'elst':elst}
    return(render(request,'truckr/payReport.html',context))

# Listing of all pay reports
def payReportList(request):
    username = request.user.username
    nav = navigation(username)
    #Pulls a list of years and months up to the current year and month
    #This should continue to work until 2064, at which point we will need to add more years into the 'years' table
    #That's a simple 'INSERT INTO years SELECT max(year) + 1 FROM years;' for as may years as you like
    lst = yearmonth.objects.raw("SELECT * FROM truckr_yearmonth WHERE period <= strftime('%Y%m',date()) ORDER BY period DESC;")
    context = {'nav':nav,'lst':lst}
    return(render(request,'truckr/payReportList.html',context))

#monthly shipments report
def shipReport(request,year,month):
    username = request.user.username
    nav = navigation(username)
    #Format year/month to single field for filtering
    period = str(year) + str('{:02d}'.format(month))
    #incoming shipments
    inlist = shipmentIn.objects.raw("select shipID, strftime('%Y%m',departure) as period, strftime('%Y',departure) as year, strftime('%m', departure) as month, strftime('%d', departure) as day, arrived,payment, clientName, costShippingHandling, productTotal FROM truckr_shipmentin join truckr_purchaseorder on truckr_shipmentin.purchaseOrder = truckr_purchaseorder.purchaseOrderID join vw_purchaseOrderTotal on truckr_shipmentin.purchaseOrder = vw_purchaseOrderTotal.purchaseOrderID WHERE period = '{}' ;".format(period))
    #Outgoing shipments
    outlist = shipmentOut.objects.raw("Select shipID, strftime('%Y%m',departure) as period, strftime('%Y',departure) as year, strftime('%m', departure) as month, strftime('%d', departure) as day, arrived,payment, clientName, costShippingHandling, productTotal FROM truckr_shipmentout join truckr_purchaseorder on truckr_shipmentout.purchaseOrder = truckr_purchaseorder.purchaseOrderID join vw_purchaseOrderTotal on truckr_shipmentout.purchaseOrder = vw_purchaseOrderTotal.purchaseOrderID WHERE period = '{}' ;".format(period))
    context = {'nav':nav,'inlist':inlist,'outlist':outlist}
    return(render(request,'truckr/shipReport.html',context))

#List of shipping reports
def shipReportList(request):
    username = request.user.username
    nav = navigation(username)
    #This lists all months up to current. I would like to have only listed relavent months, but I couldn't figure out an appropriate select query to join either of the two shipment tables.
    #I also tried creating a 3rd table that automatically inserted new months, but I couldn't get Django to run them.
    lst = yearmonth.objects.raw("SELECT * FROM truckr_yearmonth WHERE period <= strftime('%Y%m',date()) ORDER BY period DESC;")
#    lst = yearmonth.objects.raw("SELECT * FROM truckr_yearmonth JOIN ship_report_list ON truckr_yearmonth.period = ship_report_list.period ORDER BY truckr_yearmonth.period DESC;")
    context = {'nav':nav,'lst':lst}
    return(render(request,'truckr/shipReportList.html',context))
