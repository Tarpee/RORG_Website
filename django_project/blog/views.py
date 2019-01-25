from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def page1(request):
    return render(request, 'blog/page1.html')

def page2(request):
    return render(request, 'blog/page2.html')

def page3(request):
    return render(request, 'blog/page3.html')

def page4(request):
    return render(request, 'blog/page4.html')

def page5(request):
    return render(request, 'blog/page5.html')

def page6(request):
    return render(request, 'blog/page6.html')

def page7(request):
    return render(request, 'blog/page7.html')

def page8(request):
    return render(request, 'blog/page8.html')

def page9(request):
    return render(request, 'blog/page9.html')
