from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse
from trackify.models import User, UserProfile, Finance


# Create your views here.

def index(request):
    return render (request, 'trackify/index.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

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

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "trackify/register.html", {
                "message": "Passwords must match."
            })
        if User.objects.filter(username=username).exists():
            return render(request, "trackify/register.html", {
                "message": "Username already taken."
            })
        
        user = User.objects.create_user(username='username', email='email@example.com', password='password')

        # Attempt to create new user
        try:
            user_data = UserProfile.objects.create(
                username,
                email,
                password, 
                first_name=firstname, 
                last_name=lastname,
                occupation = occupation
                )
            user_data.save()
        except IntegrityError:
            return render(request, "trackify/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "trackify/register.html")
