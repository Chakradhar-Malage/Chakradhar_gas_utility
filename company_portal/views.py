# from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from django.contrib.auth.views import LogoutView


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world</h1>')

def Chiku(request):
    return render(request, "company_portal/homepage.html")

def homepage(request):
    return render(request, 'homepage.html')

def login_page(request):
    return render(request, "company_portal/login_page.html")

def login_emp_page(request):
    return render(request, "company_portal/login_emp_page.html")

def reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login_page/')  # Redirect to login page after successful registration
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'company_portal/reg.html')

@login_required
def logged_in(request):
    return render(request, 'company_portal/logged_in.html')

def request_services(request):
    return render(request, "company_portal/request_services.html")

def submit_request(request):
    if request.method == 'POST':
        # Process the form data here
        service_category = request.POST.get('service_category')
        request_details = request.POST.get('request_details')

        # Save the request (this part assumes you have already defined your ServiceRequest model)
        ServiceRequest.objects.create(
            service_category=service_category,
            request_details=request_details
        )

        # Add success message
        messages.success(request, 'Service request submitted successfully!')

        # Redirect to a different page or the same page to show the popup
        return redirect('request_services')  # Redirect to the services page or home page
    else:
        return redirect('request_services')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse('Invalid login credentials.')

        user = authenticate(request, username=user.username, password=password)
        
        if user is not None:
            login(request, user)  # Use renamed login function
            return redirect('logged_in')  # Redirect after successful login
        else:
            return HttpResponse('Invalid login credentials.')
    
    return render(request, 'company_portal/login_page.html')

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'company_portal/request_tracking.html', {'requests': requests})

