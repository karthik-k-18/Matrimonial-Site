#import path
from django.urls import path
#import views from SiteApp
from SiteApp.views import index

urlpatterns = [
    path("", index, name="index"),


    

]
