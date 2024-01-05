from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "finance/finance_index.html")

def financial_activities(request):
    
    return render(request, "finance/activities.html")

def beneficiaries(request):
    return render(request, "finance/beneficiaries.html")

def profile(request):
    return render(request, "finance/profile.html")

def login_register(request):
    return render(request, "finance/finance_login.html")