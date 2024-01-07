from .models import *
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
login_url = "/projects/finance-app/login/"
# Create your views here.
@login_required(login_url=login_url)
def index(request):
        
    return render(request, "finance/finance_index.html")
    

@login_required(login_url=login_url)
def financial_activities(request):
    
    return render(request, "finance/activities.html")

@login_required(login_url=login_url)
def beneficiaries(request):
    return render(request, "finance/beneficiaries.html")


@login_required(login_url=login_url)
def profile(request):
    return render(request, "finance/profile.html")

def login_register(request):
    if request.method == "POST":
        formType = request.POST.get("submit_type")

        # --- runs if the from information is from the register page
        # --------------------------------------------------------------------------------------------------
        if formType == "register":
            username = request.POST.get("username")
            firstname = request.POST.get("firstname")
            surname = request.POST.get("surname")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirmPassword = request.POST.get("confirmPassword")

            # check if username already exists
            if userExists:= User.objects.filter(username=username).exists():
                return render (request, "finance/finance_login.html", {
                "notification":"User already Exists"
            })

            # check if passwords match  
            elif password != confirmPassword:
                return render (request, "finance/finance_login.html", {
                "notification":"Passwords Dont match"
            })
            newUser = User.objects.create(username=username, first_name=firstname, last_name=surname, email=email, password=password)
            newUser.save()

            return render (request, "finance/finance_login.html", {
                "notification":"Saved Successfully"
            })
        

        # --- runs if the form is from login page 
        # --------------------------------------------------------------------------------------------------------
        elif formType == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if not user:
                return render(request, "finance/finance_login.html",{
                    "notification": "User Doesn't Exist",
                })
            login(request, user)
            return redirect("finance_index")
        
    logout(request)
    return render(request, "finance/finance_login.html")