"""
Landlord_App Views Module

This module contains functions that support all logic for addiing, removing,
updating, and displaying data associated with the Landlord_app.
"""

import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Unit, State, Tenant


def index(request):
    """
    Render the default view.
    """
    if request.user.is_authenticated:
        return render(request, "landlord_app/landing_page.html")
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


@login_required
def update_unit(request):
    """
    Given a request via POST, creates an instance of Unit with the request
    payload and saves the unit.
    """

    if request.method == 'POST':

        d = json.loads(request.body)
        data = d["childunit"]
        print(data)

        # Get the state object associate with the pk submitted from request
        state = State.objects.get(pk=data["state"])

        # Create an instance of Unit with attributes from request
        newunit = Unit(
            nickname=data["nickname"],
            address_line1=data["address_line1"],
            city=data["city"],
            state=state,
            zipcode=data["zipcode"],
            owner=request.user
        )

        # Handle conditional address_line2 field
        if 'address_line2' in data.keys():
            newunit.address_line2 = data["address_line2"]

        newunit.save()
        return JsonResponse({"message": "New unit saved successfully.", "id": newunit.id}, status=201)

    elif request.method == 'PUT':

        # Retrieve the specified Unit Object
        d = json.loads(request.body)
        data = d["childunit"]
        print(data)
        unit = Unit.objects.get(id=data["id"])

        # Confirm that the requestor is the owner of the unit
        if request.user == unit.owner:

            # Get the state object associate with the pk submitted from request
            state = State.objects.get(pk=data["state"])

            # Update unit attributes
            unit.nickname = data["nickname"]
            unit.address_line1 = data["address_line1"]
            unit.address_line2 = data["address_line2"]
            unit.city = data["city"]
            unit.state = state
            unit.zipcode = data["zipcode"]

            # Handls conditional address_line2 field
            if 'address_line2' in data.keys():
                unit.address_line2 = data["address_line2"]

            unit.save()
            return JsonResponse({"message": "Unit updated successfully."}, status=201)

        return JsonResponse({"error": "User is not the owner of this unit."}, status=400)

    else:
        return render(request, 'landlord_app/add_unit.html')


@login_required
def delete_unit(request):
    """
    Given a unit ID via 'PUT', delete the corresponding unit from the DB only if
    the requestor is the owner of that unit.
    """
    if request.method != 'PUT':
        return JsonResponse({"error": "PUT method required."}, status=400)

    d = json.loads(request.body)
    data = d["childunit"]
    print(data)
    unit = Unit.objects.get(id=data["id"])

    if request.user == unit.owner:

        unit.delete()
        return JsonResponse({"message": "Unit deleted successfully."}, status=201)

    return JsonResponse({"error": "User is not the owner of this unit."}, status=400)


@login_required
def update_tenant(request):
    """
    Given a tenant's data via POST or PUT, create or update the Tenant instance
    only if the requestor is the owner of the associated unit.
    """
    if request.method == 'POST':

        d = json.loads(request.body)
        data = d["childtenant"]
        print(data)

        # Get the Unit associated with this tenant
        unit = Unit.objects.get(pk=data["unit_id"])

        # Confirm that the user is the owner of the unit involved
        if request.user == unit.owner:

            # Create an instance of Unit with attributes from request
            newtenant = Tenant(
                tenant_first=data["tenant_first"],
                tenant_last=data["tenant_last"],
                tenant_email=data["tenant_email"],
                unit=unit
            )

            newtenant.save()
            return JsonResponse({"message": "New tenant saved successfully.", "id": newtenant.id}, status=201)

        return JsonResponse({"error": "User is not the owner of this unit."}, status=400)

    elif request.method == 'PUT':

        d = json.loads(request.body)
        data = d["childtenant"]
        print(data)

        # Get the Unit associated with this tenant
        unit = Unit.objects.get(pk=data["unit_id"])

        # Confirm that the user is the owner of the unit involved
        if request.user == unit.owner:

            # Get the tenant specified in the request
            tenant = Tenant.objects.get(pk=data["id"])

            # Update tenant attributes and save the tenant
            tenant.tenant_first = data["tenant_first"]
            tenant.tenant_last = data["tenant_last"]
            tenant.tenant_email = data["tenant_email"]
            tenant.save()

            return JsonResponse({"message": "Tenant updated successfully."}, status=201)

        return JsonResponse({"error": "User is not the owner of this unit."}, status=400)

    else:
        return JsonResponse({"error": "POST or PUT method required"}, status=400)


@login_required
def delete_tenant(request):
    """
    Given a tenant ID via 'PUT', delete the corresponding tenant from the DB only if
    the requestor is the owner of the corresponding unit.
    """
    if request.method != 'PUT':
        return JsonResponse({"error": "PUT method required."}, status=400)

    d = json.loads(request.body)
    data = d["childtenant"]
    print(data)

    # Get the unit associated with this tenant
    unit = Unit.objects.get(pk=data["unit_id"])

    # Confirm that the user is the owner of this unit
    if request.user == unit.owner:

        # Delete the tenant
        tenant = Tenant.objects.get(id=data["id"])
        tenant.delete()

        return JsonResponse({"message": "Tenant deleted successfully."}, status=201)

    return JsonResponse({"error": "User is not the owner of this unit."}, status=400)
