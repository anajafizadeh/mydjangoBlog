from django.shortcuts import render, HttpResponse

def about(request):
    # return HttpResponse("Hello World!")
    return render(request, 'about.html')

def home(request):
    # return HttpResponse("Home")
    return render(request, 'Home.html')