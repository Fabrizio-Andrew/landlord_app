from django.shortcuts import render
from landlord_app import util

# Here's some views:

def index(request):
    return render(request, "landlord_app/index.html", {
        "entries": util.all_properties
    })

def add_property(request):
    return render(request, "landlord_app/add_property.html")

def save_property(request):
    x = {'nicknamevalue': request.POST['nickname'], 'addressvalue': request.POST['street_address'], 'bedvalue': request.POST['bedrooms'], 'bathvalue': request.POST['bathrooms']}
    util.saveproperty(x)
    print(util.all_properties)
    return render(request, 'landlord_app/index.html', {

    })
