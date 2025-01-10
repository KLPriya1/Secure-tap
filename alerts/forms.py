from django import forms
from .models import Contact, Alert


# forms.py

from django import forms
from .models import Alert

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['message', 'location']  # Ensure 'message' and 'location' are present

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Set default message and location in form initialization
        if not self.instance.pk:  # Only set if creating a new alert (not editing)
            self.fields['message'].initial = 'ALERT'
            self.fields['location'].initial = 'kovvada'


from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number']

from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
