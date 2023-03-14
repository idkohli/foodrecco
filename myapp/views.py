from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
import pyrebase
import random

config={
    "apiKey": "AIzaSyA7K1QZ2LN4rdB1WcgRxQo3fpYRxxAyNCg",
    "authDomain": "mealreccomender.firebaseapp.com",
    "databaseURL": "https://mealreccomender-default-rtdb.firebaseio.com",
    "projectId": "mealreccomender",
    "storageBucket": "mealreccomender.appspot.com",
    "messagingSenderId": "530024628439",
    "appId": "1:530024628439:web:cbeb565992ba0b680db092"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def index(request):
    if request.method == 'POST' and request.action == 'add':
        return render(request, 'add.html')
    elif request.method == 'POST' and request.action == 'recco':
        return render(request, 'recco.html')
    else:
        return render(request, 'index.html')

def recco(request):

    length = len(database.child('Lunch').get().val()) - 1
    id = random.randint(1, length)
    meal = database.child('Lunch').child(id).child('Name').get().val()
    recipe = database.child('Lunch').child(id).child('Recipe').get().val()
    return render(request, 'recco.html', {
        "meal": meal,
        "recipe": recipe
    })


def add(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Recipe = request.POST.get('recipe')
        Id = len(database.child('Lunch').get().val())
        data = {"Name": Name, "Recipe": Recipe}
        database.child('Lunch').child(Id).set(data)
        return render(request, 'add.html')
    else:
        return render(request, 'index.html')

"""
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else: 
            messages.info(request, 'Credentials invalid!')
            return redirect('login')
    else: 
        return render(request, 'login.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
"""