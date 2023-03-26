from django.contrib import admin
from django.urls import path, include
from . import views

#from here it goes to home and the other things will be accessed through buttons

urlpatterns = [
path('', views.home, name="home"),
path('signup', views.signup, name="signup"),
path('signin', views.signin, name="signin"),
path('signout', views.signout, name="signout"),
]