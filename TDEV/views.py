from django.shortcuts import render
from .forms import *
from django.views import View
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request, "index.html")


class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! You are  Registered Successfully ")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'register.html', locals())