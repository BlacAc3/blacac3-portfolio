from django.shortcuts import render
from django.http import request
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60*15)
def index(request):
    return render(request, "main/main_index.html")