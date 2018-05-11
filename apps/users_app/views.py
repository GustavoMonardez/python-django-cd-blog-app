from django.shortcuts import render, HttpResponse, redirect

def register(request):
    return HttpResponse("This is the users' register page")

def login(request):
    return HttpResponse("This is the login users' page")

def users(request):
    return HttpResponse("This is the users' index page")

def users_new(request):
    return HttpResponse("This is the users' new page")

