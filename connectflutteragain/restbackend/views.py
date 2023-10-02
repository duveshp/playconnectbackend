# from django.shortcuts import render

# Create your views here.
from .forms import VendorRegistrationForm,VendorLoginForm
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import PlayAreaDB,VendorDB,UserDB,BookingDB,AdminDB
from .serializers import PlayAreaSerializer,VendorSerializer,UserSerializer,BookingSerializer,AdminSerializer
from django.contrib.auth import authenticate, login

class PlayAreaViewSet(viewsets.ModelViewSet):
    queryset = PlayAreaDB.objects.all()
    serializer_class = PlayAreaSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = VendorDB.objects.all()
    serializer_class = VendorSerializer

from django.contrib.auth import authenticate, login
def authenticate_vendor(email, password):
    try:
        # Attempt to retrieve a vendor with the provided email
        vendor = VendorDB.objects.get(VendorEmail=email)
    except VendorDB.DoesNotExist:
        return None  # Vendor with the provided email doesn't exist

    if vendor.VendorPassword == password:
        return vendor  # Authentication successful
    else:
        return None  # Invalid password

def vendor_login(request):
    if request.method == 'POST':
        form = VendorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['vendor_email']
            password = form.cleaned_data['vendor_password']
            
            # Authenticate the vendor
            vendor = authenticate_vendor(email, password)
            if vendor is not None:
                # Log in the vendor (you can store the vendor's information in the session)
                request.session['vendor_id'] = vendor.id
                
                # Redirect to the vendor's dashboard or another page upon successful login
                return redirect('vendor_area')
            else:
                # Authentication failed, handle the error
                return render(request, 'vendor_login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = VendorLoginForm()

    return render(request, 'vendor_login.html', {'form': form})

def vendor_registration(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle success or redirection here
            return redirect('success_page')
    else:
        form = VendorRegistrationForm()

    return redirect('vendor_login')  

def vendor_area(request):
    # Your view logic here
    return render(request, 'vendor_area.html')



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDB.objects.all()
    serializer_class = UserSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingDB.objects.all()
    serializer_class = BookingSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = AdminDB.objects.all()
    serializer_class = AdminSerializer

