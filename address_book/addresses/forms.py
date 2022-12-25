from django import forms
from django.forms import ModelForm
from .models import Client, Address

# Create a address and client forms


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('street_name', 'street_number', 'city', 'zip_code', 'country')
        labels = {
            "street_name": '',
            "street_number": '',
            "city": '',
            "zip_code": '',
            "country": '',
        }

        widgets = {
            "street_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Name'}),
            "street_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Number'}),
            "city": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
            "zip_code": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            "country": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email_address', 'phone')
        labels = {
            "first_name": '',
            "last_name": '',
            "email": '',
            "phone": '',
        }

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Number'}),
            "email_address": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        }
