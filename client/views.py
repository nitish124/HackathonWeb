from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = 'login')
def client_dashboard(request):
    return render(request, 'client/client_dashboard.html')

@login_required(login_url = 'login')
def loyalty_dashboard(request):
    return render(request, 'client/loyalty_dashboard.html')