import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from landlord_app import util

from .models import User, Unit

# Here's some views:

def index(request):
    """
    Render the default view.
    """
    return render(request, 'landlord_app/index.html')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("landing"))
        else:
            return render(request, "landlord_app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "landlord_app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "landlord_app/register.html", {
                "message": "Passwords must match."
            })
        user = User(username=request.POST["email"],
        email=request.POST["email"],
        first_name=request.POST["firstname"],
        last_name=request.POST["lastname"],
        address_line1=request.POST["street1"],
        address_line2=request.POST["street2"],
        city=request.POST["city"],
        state=request.POST["state"],
        zipcode=request.POST["zipcode"])

        # Hash and save password
        user.set_password(password)

        # Attempt to create new user
        try:
            user.save()
        except IntegrityError:
            return render(request, "landlord_app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("landing"))
    else:
        return render(request, "landlord_app/register.html")

@login_required
def landing_page(request):
    return render(request, 'landlord_app/landing_page.html')

@login_required
def get_units(request):
    """
    Returns all instances of Unit belonging to the currently authenticated user.
    """

    user = request.user
    units = Unit.objects.filter(owner=user)
    return JsonResponse([unit.serialize() for unit in units], safe=False)

def add_unit(request):
    return render(request, 'landlord_app/add_unit.html')


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
    #for unit in util.list_units():



    return render(request, 'landlord_app/index.html', {
        'units': util.list_units_detailed

    })
