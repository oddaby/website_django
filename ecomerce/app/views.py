from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegistrationForm
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def home(request):
    return render(request, 'users/home.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')







def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Extract form data
            username = form.cleaned_data.get('username')
            # Redirect to the success page or home page with success message
            messages.success(request, 'Registration successful!')
            return redirect('/home.html')
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})




def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Change 'home' to the appropriate URL name for your home page
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


