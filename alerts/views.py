from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AlertForm, ContactForm
from .models import Contact, Alert
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'alerts/home.html')  # Correct path to the template

# Send alert to all contacts
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AlertForm
from .models import Alert
from django.contrib.gis.geoip2 import GeoIP2  # You may need to install this for geolocation

@login_required
def send_alert(request):
    if request.method == 'POST':
        # When the form is submitted, create an alert with the custom message
        form = AlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user  # Associate the alert with the logged-in user
            alert.save()

            # Send alert to all contacts
            for contact in request.user.contacts.all():  # Get contacts for this user
                alert.contacts.add(contact)  # Add contacts to alert
            alert.save()

            return redirect('alert_success')
    else:
        # Default message and location
        default_message = "HELP"
        location = "Vit, Kovvada, Bhimavaram, WGdist, AP"  # Default location or get the real location if you have geolocation data
        # GeoIP2 or other geolocation service can be used here to get user's actual location

        # You can pre-populate the form with the default message and location
        form = AlertForm(initial={'message': default_message, 'location': location})

    return render(request, 'alerts/send_alert.html', {'form': form})



# Success page after alert is sent
def alert_success(request):
    return render(request, 'alerts/alert_success.html')


# List of contacts for the logged-in user
@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)  # Get contacts for the logged-in user
    return render(request, 'alerts/contact_list.html', {'contacts': contacts})


# Add a new contact for the logged-in user
@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user  # Associate the contact with the logged-in user
            contact.save()
            return redirect('contact_list')  # Redirect to the contact list after adding the contact
    else:
        form = ContactForm()

    return render(request, 'alerts/add_contact.html', {'form': form})


# Delete a contact for the logged-in user
@login_required
def delete_contact(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id, user=request.user)
        if request.method == 'POST':
            contact.delete()  # Delete the contact
            return redirect('contact_list')  # Redirect to the contact list after deletion
    except Contact.DoesNotExist:
        pass  # Contact not found for this user, handle gracefully

    return render(request, 'alerts/delete_contact.html', {'contact': contact})


# View all alerts sent by the logged-in user
@login_required
def user_alerts(request):
    alerts = Alert.objects.filter(user=request.user)  # Get alerts for the logged-in user
    return render(request, 'alerts/user_alerts.html', {'alerts': alerts})

from .forms import SignUpForm

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Or wherever you'd like to redirect after signup
    else:
        form = UserCreationForm()
    return render(request, 'alerts/signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Or wherever you'd like to redirect after signup
    else:
        form = UserCreationForm()
    return render(request, 'alerts/signup.html', {'form': form})