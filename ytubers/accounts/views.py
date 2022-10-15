from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):

    if not request.user.is_authenticated:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)

                messages.success(request, "Logged In Successfully.")
                return redirect('dashboard')

            else:
                messages.error(request, "Invalid Credentials.")
                return redirect('login')

        return render(request, 'accounts/login.html')

    else:
        return redirect('dashboard')
    


def register(request):

    if not request.user.is_authenticated:

        if request.method == 'POST':
            firstname = request.POST['first_name'].capitalize()
            lastname = request.POST['last_name'].capitalize()
            username = request.POST['username'].lower()
            email = request.POST['email'].lower()
            password = request.POST['password']
            password2 = request.POST['password2']

            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already registered.")
                    return redirect('register')

                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, "Email already registered.")
                        return redirect('register')
                    else:
                        user = User.objects.create_user(
                            first_name=firstname, last_name=lastname,
                            username=username, email=email,
                            password=password
                        )

                        user.save()
                        messages.success(request, "Account Created Successfully.")
                        return redirect("login")
        
        return render(request, 'accounts/register.html')

    return redirect('dashboard')


def logout_user(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    
    return render(request, 'accounts/dashboard.html')
