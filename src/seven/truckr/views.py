from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from truckr.models import employee,product,purchaseOrder,orderItem,shipmentIn, shipmentOut,navbar


# Create your views here.
#showes stuff to the webpage that the user can see
def home(request):
    username = request.user.username
    nav = navbar.objects.raw("""
                SELECT * FROM truckr_employee 
                JOIN truckr_account ON truckr_employee.employeeID = truckr_account.employeeID 
                JOIN truckr_navbar ON truckr_account.accountType = truckr_navbar.accountType
                WHERE truckr_employee.username = '%s';
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
            fname = user.first_name
            nav = navbar.objects.raw("""
                SELECT * FROM truckr_employee 
                JOIN truckr_account ON truckr_employee.employeeID = truckr_account.employeeID 
                JOIN truckr_navbar ON truckr_account.accountType = truckr_navbar.accountType
                WHERE truckr_employee.username = '%s';
            """ % username)
            return render(request, "truckr/index.html", {'nav': nav})
            #return render(request, "truckr/index.html", {'fname': fname})
        
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
    elist = employee.objects.order_by('employeeID')
    context = {'elist': elist}
    return(render(request, 'truckr/employees.html', context))

def products(request):
    plist = product.objects.order_by('productID')
    context = {'plist': plist}
    return(render(request, 'truckr/products.html', context))

def purchaseOrders(request):
    polist  = purchaseOrder.objects.order_by('purchaseOrderID')
    context = {'polist':polist}
    return(render(request, 'truckr/purchaseOrders.html', context))

def purchaseOrderDetail(request, ID):
    # Join the orderitem table with the product table to display product data for that order. Filters for a specific purchase order
    items = orderItem.objects.raw('SELECT truckr_orderitem.id as id, truckr_orderitem.purchaseOrderID as purchaseOrderID, truckr_orderitem.productID as productID, truckr_product.productName as productName, truckr_product.price as price, truckr_orderitem.quantity as quantity, truckr_orderitem.status as status FROM truckr_orderitem INNER JOIN truckr_product ON truckr_orderitem.productID = truckr_product.productID WHERE truckr_orderitem.purchaseOrderID = %s', [ID])
#inferior code    items = orderItem.objects.filter(purchaseOrderID = ID)
    context = {'items':items}
    return(render(request, 'truckr/purchaseOrdersDetail2.html', context))

def shipmentsIn(request):
    username = request.user.username

    lst = shipmentIn.objects.raw("SELECT * from truckr_shipmentin JOIN truckr_employee ON truckr_shipmentin.driver = truckr_employee.employeeID WHERE truckr_employee.username = '%s';" % username)
    context = {'lst':lst}
    return(render(request, 'truckr/shipmentsIn.html', context))

def shipmentsOut(request):
    username = request.user.username

    lst = shipmentOut.objects.raw("SELECT * from truckr_shipmentout JOIN truckr_employee ON truckr_shipmentout.driver = truckr_employee.employeeID WHERE truckr_employee.username = '%s';" % username)
    context = {'lst':lst}
    return(render(request, 'truckr/shipmentsOut.html', context))

