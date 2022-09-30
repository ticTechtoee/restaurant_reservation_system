from .models import Menu
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import  render, redirect

def menu_navbar(request):
    menu_item = Menu.objects.all()
    return {
        'menu_item' : menu_item
    }

def logout_request(request):
	logout(request)
	return redirect("login")
