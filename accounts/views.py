from django.shortcuts import render, redirect
from .forms import RegistrationForm
from accounts.models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
	#This request.POST will contain all the field's values
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #We use cleaned_data to fetch the values from the request
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            status = form.cleaned_data['status']
        
        user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.phone_number = phone_number
        user.status = status
        user.save()
    else:
        #It is only a GET request to get the form
        form = RegistrationForm()
    context = {
        'form': form,
    }   
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email'] #it takes the value from the name we added in the input
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now login')
            return redirect('client_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Thanks for spending some quality time with us today.')
    return redirect('login')

def forgot_password(request):
    return render(request, 'accounts/forgot-password.html')