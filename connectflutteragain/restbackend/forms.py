from django import forms
from .models import VendorDB

class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = VendorDB
        fields = '__all__'  # You can specify the fields you want to include

class VendorLoginForm(forms.Form):
    vendor_email = forms.EmailField(label='Email', max_length=100, required=True)
    vendor_password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput, required=True)
