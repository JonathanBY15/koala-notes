from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def home_view(request):
    """Display the homepage."""

    return render(request, 'home.html')

def register_view(request):
    """Register a new user."""

    if request.method == 'POST':
        # Grab the data from the user's submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database and redirect to homepage
            form.save()
            return redirect('home')
    else:
        # Display a blank registration form
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form, 'user': request.user})

def login_view(request):
    """Log in an existing user."""

    if request.method == 'POST':
        # Grab the data from the user's submission
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user and redirect to homepage
            login(request, form.get_user())
            return redirect('home')
    else:
        # Display a blank login form
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    """Log out the current user."""
    if request.method == 'POST':
        # Log out the user and redirect to homepage
        logout(request)
        return redirect('login')