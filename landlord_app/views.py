import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from landlord_app import util

from .models import User, Unit, State

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

# OBSOLETE
def add_unit(request):
    return render(request, 'landlord_app/add_unit.html')

@login_required
def new_unit(request):
    """
    Given a request via POST, creates an instance of Unit with the request
    payload and saves the unit.
    """
    
    if request.method != 'POST':
        return render(request, 'landlord_app/add_unit.html')
    
    data = json.loads(request.body)
    newunit = Unit(
        nickname=data["nickname"],
        address_line1=data["address.line1"],
        address_line2=data["address_line2"],
        city=data["city"],
        state=data["state"],
        zipcode=data["zipcode"],
        owner=request.user
    )
    newunit.save()
    return JsonResponse({"message": "Unit saved successfully."}, status=201)

@login_required
def update_unit(request):
    """
    Given an existing unit's ID and updated attributes, update the Unit object's
    attributes only if the currently logged-in user is the owner of the unit.
    """

    if request.method != 'PUT':
        return JsonResponse({"error": "PUT request required."}, status=400)

    # Retrieve the specified Unit Object
    data = json.loads(request.body)
    unit = Unit.objects.get(id=data["unit_id"])

    # Confirm that the requestor is the owner of the unit
    if request.user == unit.owner:

        # Update unit attributes and save
        unit.nickname = data["nickname"]
        unit.address_line1 = data["address_line1"]
        unit.address_line2 = data["address_line2"]
        unit.city = data["city"]
        unit.zipcode = data["zipcode"]
        unit.save()
        return JsonResponse({"message": "Unit updated successfully."}, status=201)
    
    return JsonResponse({"error": "User is not the owner of this unit."}, status=400)




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
    #for unit in util.list_units()



    return render(request, 'landlord_app/index.html', {
        'units': util.list_units_detailed

    })

def eviction_tree(request):
    return render(request, 'landlord_app/evict_tree.html')

def state_rules(request, state):
    """
    Given a state abbreviation, provides a JSON output of relevant laws for that state.
    """
    requestedstate = State.objects.get(abbrev=state.upper())
    serialized = requestedstate.serialize()
    return JsonResponse(serialized, safe=False)