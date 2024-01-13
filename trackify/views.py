from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse
from trackify.models import NewUser, Finance


# Create your views here.

def index(request):
    return render (request, 'trackify/index.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "trackify/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "trackify/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        occupation = request.POST["occupation"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Ensure password matches confirmation
        if password != confirmation:
            return render(request, "trackify/register.html", {
                "message": "Passwords must match."
            })

        # Check for duplicate username
        if NewUser.objects.filter(username=username).exists():
            return render(request, "trackify/register.html", {
                "message": f"Username {username} already taken."
            })

        # Attempt to create new user
        user = NewUser.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.occupation = occupation
        user.save()

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "trackify/register.html")
