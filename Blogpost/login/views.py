from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . models import Info
from django.views.generic import ListView,DetailView

# Create your views here.
def home(request):

    return render(request,'home.html')
def login(request):
    pass
def signup(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
    else:
        form= UserCreationForm()
    return render(request,'signup.html',{'form':form})

