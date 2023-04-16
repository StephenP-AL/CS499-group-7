from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from truckr.models import employee,product,purchaseOrder,orderItem,shipmentIn, shipmentOut,navbar,manifest,manifestItem,vehicle,part,partsList,maintenance


# Create your views here.
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

def employees(request):
    username = request.user.username
    nav = navigation(username)
    elist = employee.objects.order_by('employeeID')
    context = {'elist': elist, 'nav': nav}
    return render(request, 'truckr/employees.html', context)

def products(request):
    username = request.user.username
    nav = navigation(username)

    plist = product.objects.order_by('productID')
    context = {'plist': plist,'nav': nav}
    return render(request, 'truckr/products.html', context)

def purchaseOrders(request):
    username = request.user.username
    nav = navigation(username)

    polist  = purchaseOrder.objects.order_by('purchaseOrderID')
    context = {'polist':polist,'nav': nav}
    return(render(request, 'truckr/purchaseOrders.html', context))

def purchaseOrderDetail(request, ID):
    username = request.user.username
    nav = navigation(username)
    po = purchaseOrder.objects.raw('SELECT * FROM truckr_purchaseorder WHERE purchaseOrderID = %s;',[ID])

    # Join the orderitem table with the product table to display product data for that order. Filters for a specific purchase order
    items = orderItem.objects.raw('SELECT truckr_orderitem.id as id, truckr_orderitem.purchaseOrderID as purchaseOrderID, truckr_orderitem.productID as productID, truckr_product.productName as productName, truckr_product.price as price, truckr_orderitem.quantity as quantity, truckr_orderitem.status as status FROM truckr_orderitem INNER JOIN truckr_product ON truckr_orderitem.productID = truckr_product.productID WHERE truckr_orderitem.purchaseOrderID = %s', [ID])

    context = {'items':items,'nav':nav, 'po':po}
    return(render(request, 'truckr/purchaseOrdersDetail2.html', context))

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

def maintenanceReport(request, year, month):
    username = request.user.username
    nav = navigation(username)
    yr = str(year)
    mo = str('{:02d}'.format(month))
    
    maint = maintenance.objects.raw("SELECT * FROM maintenance_rpt_bymonth WHERE yr = '{}' and mo = '{}';".format(yr,mo))
    context = {'nav':nav,'maint':maint}
    return(render(request, 'truckr/maintenanceReport.html', context))
