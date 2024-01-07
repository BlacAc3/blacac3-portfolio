from .models import *
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import random





login_url = "/projects/finance-app/login/"
# Create your views here.
@login_required(login_url=login_url)
def index(request):
    user = request.user
    user_set = user.account.first()
    balance = user_set.balance
    return render(request, "finance/finance_index.html",{
        "balance":balance,
    })
    

@login_required(login_url=login_url)
def financial_activities(request):
    
    return render(request, "finance/activities.html")

@login_required(login_url=login_url)
def beneficiaries(request):
    return render(request, "finance/beneficiaries.html")


@login_required(login_url=login_url)
def profile(request):
    user = request.user
    account = User_account.objects.get(user=user)
    return render(request, "finance/profile.html", {
        "user":user,
        "account_number":account.accountNumber,
    })


# Function that handles login, logout and registration 
# ------------------------------------------------------------------------------------------------
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
            newAccount = User_account.objects.create(user=newUser, accountNumber = accountNumberGenerator())
            newAccount.save()

            return render (request, "finance/finance_login.html", {
                "notification":"Saved Successfully"
            })
        

        # --- runs if the form is from login page 
        # --------------------------------------------------------------------------------------------------------
        elif formType == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")
            userCheckUsername = User.objects.filter(username=username).exists()
            userCheckPassword= User.objects.filter(username=username, password=password).exists()
            if not userCheckUsername:
                return render(request, "finance/finance_login.html",{
                    "notification": "User Doesn't Exist",
                })
            elif userCheckUsername and not userCheckPassword:
                return render(request, "finance/finance_login.html",{
                    "notification": "Wrong Password",
                })
            

            #if user already has an account in other projects add the user to this project account models so as to prevent errors
            #users from other projects account are visible universally so existing users are required to simply login and the required informarion will be added
            user = User.objects.get(username = username)
            account = User_account.objects.filter(user = user).exists()
            if not account:
                newAccount=User_account.objects.create(user=user, accountNumber = accountNumberGenerator())
                newAccount.save()
            login(request, user)
            return redirect("finance_index")
        
    logout(request)
    return render(request, "finance/finance_login.html")


def accountNumberGenerator():
    mode = "running"
    randNum= None
    while mode == "running":
        randNum = random.randint(10**10, (10**11)-1)
        user = User_account.objects.filter(accountNumber = randNum).exists()
        if not user:
            mode="stopped"
    return randNum

