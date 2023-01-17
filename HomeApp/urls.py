#import path
from django.urls import path
#import views from SiteApp
from HomeApp.views import index

urlpatterns = [
    path("", index, name="index"),
]
