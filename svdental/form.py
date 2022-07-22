from django import forms
from .models import Appointment

class AppoinmentForm(forms.ModelForm):
    customerName = forms.CharField(label='Tên khách hàng', max_length=100)

    email = forms.EmailField(label="Email", max_length= 100)

    phoneNumber = forms.CharField(label="Số điện thoại", max_length=200)

    class Meta:
        model = Appointment
        fields = ['customerName', 'email', 'phoneNumber']
