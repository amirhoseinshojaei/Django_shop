from .models import Order
from django import forms
class CreateOrderForm(forms.ModelForm):
    CITY_LIST = [
        ('a', 'New York'),
        ('b', 'Los Angles'),
        ('c', 'Texas'),
        ('d', 'San Francisco'),
    ]
    first_name = forms.CharField(max_length=255,label='Enter your name')
    last_name = forms.CharField(max_length=255,label='Enter your last name')
    email = forms.EmailField(label='Enter Your Email')
    city = forms.ChoiceField(choices=CITY_LIST,label='Chose your city',widget=forms.Select)
    address = forms.CharField(max_length=255,label="Enter your address")
    postal_code = forms.CharField(max_length=255,label='Enter Your postal(IMPORTANT)')
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','city','address','postal_code']