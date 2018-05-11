from django.shortcuts import render, HttpResponse, redirect

def surveys(request):
    return HttpResponse("This is the surveys' index page")

def surveys_new(request):
    return HttpResponse("This is the add new surveys' page")
