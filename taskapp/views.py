from django.shortcuts import render, HttpResponse

# Create your views here.
def ctb_welcome(request):
    return HttpResponse("Welcome to CTB app")