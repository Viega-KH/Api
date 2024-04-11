from django import forms
from .models import Order

class Orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'name', 'last_name', 'phone_number', 'address', 'liters' ]