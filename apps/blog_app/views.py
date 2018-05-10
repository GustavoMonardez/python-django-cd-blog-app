from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Here is where we'll display blog posts"
    return HttpResponse(response)

def new(request):
    response = "Create new blog"
    return HttpResponse(response)

def create(request):
    return redirect("/")

def show(request, number):
    #print(number)
    return HttpResponse("show method "+number )

def edit(request, number):
    return HttpResponse("editing blog "+number )

def destroy(request, number):
    print("from delete ",number)
    return redirect("/")