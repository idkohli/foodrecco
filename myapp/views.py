from django.shortcuts import render
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
        if not Name  and not Recipe :
            return render(request, 'add.html', {"submit": 0})
        else:
            Id = len(database.child('Lunch').get().val())
            data = {"Name": Name, "Recipe": Recipe}
            database.child('Lunch').child(Id).set(data)
            return render(request, 'add.html', {"submit": 1})
    else:
        return render(request, 'add.html', {"submit": 0})