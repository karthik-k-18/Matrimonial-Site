#import path
from django.urls import path
#import views from SiteApp
from SignupApp.views import index

urlpatterns = [
    path("", index, name="signup"),
]