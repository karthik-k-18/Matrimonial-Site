from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserForm
from firebase_admin import db

database = db.reference()

# Create your views here.

def index(request):
    #print the value of key "name" in the database
    print(database.child("name").get())
    return render(request, "HomeApp/index.html")
    