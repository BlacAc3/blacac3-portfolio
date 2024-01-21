from .models import *
from itertools import chain
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect 
from django.http import JsonResponse
from django.db.models import Q
import random
index_url = "finance/finance_index.html"
login_url = "/projects/finance-app/login/"



#This function returns important data needed to be rendered with the index page
def index_renderer(user, message):
    user_existence=User_account.objects.filter(user=user).exists()
    if not user_existence:
        newAccount = User_account.objects.create(user=user, accountNumber = accountNumberGenerator())
        newAccount.save()
    user_account = User_account.objects.get(user=user)
    balance = user.account.first().balance
    transactions= transactions_compiler(user)[:5]
    beneficiary_list = user_account.beneficiaries.all()[:6]
    data={
        "balance":int(balance),
        "beneficiaries":beneficiary_list,
        "transactions":transactions,
        "current_user":user,
        "popup_message":message,
        "user_account":user_account,
    }
    return data


# Create your views here.
@login_required(login_url=login_url)
def index(request):
    user=request.user
    data = index_renderer(user, "Welcome to my banking app")
    return render(request, index_url, data)


#combines two querySets
def transactions_compiler(user):
    sender_account=User_account.objects.get(user = user)
    return Transaction_user.objects.filter(
        Q(sender=sender_account) | Q(recipient=sender_account)
    ).order_by("-date_time")

@login_required(login_url=login_url)
def financial_activities(request):
    user=request.user
    transactions = transactions_compiler(user)
    return render(request, "finance/activities.html", {
        "transactions":transactions,
        "current_user":user,
    })

@login_required(login_url=login_url)
def beneficiaries(request):
    user=request.user
    user_account = User_account.objects.get(user=user)
    beneficiary_list = user_account.beneficiaries.all()
    data = index_renderer(user, "")
    return render(request, "finance/beneficiaries.html", data)


@login_required(login_url=login_url)
def profile(request):
    user = request.user
    data=index_renderer(user, "Profile")
    return render(request, "finance/profile.html", data)


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
            if not userCheckUsername:
                return render(request, "finance/finance_login.html",{
                    "notification": "User Doesn't Exist",
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


#generate random account number
def accountNumberGenerator():
    mode = "running"
    randNum= None
    while mode == "running":
        randNum = random.randint(10**10, (10**11)-1)
        user = User_account.objects.filter(accountNumber = randNum).exists()
        if not user:
            mode="stopped"
    return randNum

#check if account number exists
def check_account_number(request):
    #check balance
    if request.method != "GET":
        return
    current_user=request.user
    num = request.GET.get("q")
    user_account= User_account.objects.filter(accountNumber=num).exists()
    if not user_account:
        return JsonResponse({"error":"Invalid Account Number"})
    recipient_user_account = User_account.objects.get(accountNumber=num)
    current_user_account=User_account.objects.get(user=current_user)
    if current_user_account.user.username == recipient_user_account.user.username:
        return JsonResponse({"error":"Invalid Number"})

    return JsonResponse({"username":f"{recipient_user_account.user.username}", "user_balance":f"{current_user_account}"})


#function that sends money
def send_money(request):
    if request.method != "POST":
        return redirect(index)
    accountNumber = request.POST.get("accountNumber")
    amount = request.POST.get("amount")
    transactionNote = request.POST.get("transactionNote")
    current_user=request.user
    sender= User_account.objects.get(user=current_user)
    recipientExists = User_account.objects.filter(accountNumber = accountNumber).exists()

    #If account number is not valid
    if not recipientExists:
        data = index_renderer(request.user, "Failed!, Check account number.")
        return render(request, index_url, data)
        
    recipient = User_account.objects.get(accountNumber = accountNumber)

    #if sender account number is the same as the recipient account number
    if recipient.accountNumber == sender.accountNumber:
        data = index_renderer(request.user, "Failed!, Invalid transaction.")
        return render(request, index_url, data)

    #add to transactions
    new_transaction = Transaction_user.objects.create(sender = sender,recipient = recipient ,amount = amount, note=transactionNote, transaction_id = create_transaction_id())
    new_transaction.save()

    #update sender's main balance
    if int(amount)>int(sender.balance):
        data = index_renderer(request.user, "Insufficient Balance!")
        return render(request, index_url, data)
    
    new_balance = int(sender.balance) - int(amount)
    sender.balance = new_balance
    sender.save()

    #update receiver's balance
    new_r_balance = int(recipient.balance) + int(amount)
    recipient.balance = new_r_balance
    recipient.save()

    #add to beneficiaries if the existing beneficiary doesn't already exist
    if not Beneficiaries.objects.filter(user_account=sender, beneficiary_user=recipient).exists():
        new_beneficiaries = Beneficiaries.objects.create(user_account=sender, beneficiary_user=recipient)
        new_beneficiaries.save()

    data = index_renderer(request.user, "Sent! Successfully.")
    return render(request, index_url, data)

def create_transaction_id():
    mode = "running"
    randNum= None
    while mode == "running":
        randNum = random.randint(10**20, (10**21)-1)
        id_correct = Transaction_user.objects.filter(transaction_id=randNum).exists()
        if not id_correct:
            mode="stopped"
    return int(randNum)