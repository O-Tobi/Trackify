from django.shortcuts import render


# Create your views here.

def index(request):
    pass

def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name'],
        lastname = request.POST['last_name'],
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirm']

        #check if password matches confirmation

        if password != confirmation:
            return 