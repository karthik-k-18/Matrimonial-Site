from django.shortcuts import render
from .forms import UserForm
#import pyrebase version 4
import pyrebase


config = {
    "apiKey": "AIzaSyADjIrkH5xda-vfmZh-PwN78KWEAfI2oyM",
    "authDomain": "matrimonial-site-e7828.firebaseapp.com",
    "databaseURL": "https://matrimonial-site-e7828-default-rtdb.firebaseio.com",
    "projectId": "matrimonial-site-e7828",
    "storageBucket": "matrimonial-site-e7828.appspot.com",
    "messagingSenderId": "1072628141684",
    "appId": "1:1072628141684:web:ef518d9d5fd1e7557a0b21",
    "measurementId": "G-9EMVPREGV9"
}


firebase = pyrebase.initialize_app(config)
database = firebase.database()



# Create your views here.

def index(request):
    print(database.child("name").get().val())
    return render(request, "SiteApp/index.html")