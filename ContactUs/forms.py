
from django import forms



class ContactUsForm(forms.Form):
    full_name = forms.CharField(

        widget= forms.TextInput(
            attrs={
                'placeholder':'Full Name'
            }
        )
    )
    phone_number = forms.CharField(
        widget= forms.TelInput(
            attrs={
                'placeholder':'Mobile Number'
            }
        )
    )
    email = forms.CharField(
        
        widget= forms.EmailInput(
            attrs={
                'placeholder':'Email Address'
            }
        )
        
    )
    message = forms.CharField(
        
        widget= forms.TextInput(
            attrs={
                'placeholder':'Message',
                'class':'input_message'
            }
        )
    )
    

