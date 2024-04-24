from .models import Order
from django import forms
class CreateOrderForm(forms.ModelForm):

    first_name = forms.CharField(max_length=255,label='Enter your name')
    last_name = forms.CharField(max_length=255,label='Enter your last name')
    email = forms.EmailField(label='Enter Your Email')
    city = forms.CharField(max_length=255,label="Chose your city")
    address = forms.CharField(max_length=255,label="Enter your address")
    postal_code = forms.CharField(max_length=255,label='Enter Your postal(IMPORTANT)')
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','city','address','postal_code']