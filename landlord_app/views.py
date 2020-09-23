from django.shortcuts import render
from landlord_app import util

# Here's some views:

def index(request):
    return render(request, "landlord_app/index.html", {
        "entries": util.list_units
    })

def add_unit(request):
    return render(request, "landlord_app/add_unit.html")

def save_unit(request):
    x = {'nickname': request.POST['nickname'],
        'address_line1': request.POST['address_line1'],
        'address_line2': request.POST['address_line2'],
        'city': request.POST['city'],
        'state': request.POST['state'],
        'zipcode': request.POST['zipcode'],
        'bedrooms': request.POST['bedrooms'],
        'bathrooms': request.POST['bathrooms']
    }
    util.save_unit(x)
    print(util.list_units)
    return render(request, 'landlord_app/index.html', {

    })
