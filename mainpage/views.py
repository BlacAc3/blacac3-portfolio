from django.shortcuts import render
from django.http import request
# Create your views here.
def index(request):
    return render(request, "main/main_index.html")