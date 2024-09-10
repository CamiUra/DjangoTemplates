from django.shortcuts import render

def index(request):
    return render(request, 'App/hola.html')

def view1(request):
    return render(request, 'App/page1.html')

def view2(request):
    return render(request, 'App/page2.html')

