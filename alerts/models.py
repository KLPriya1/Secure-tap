from django.db import models
from django.contrib.auth.models import User  # Import once

# Contact Model: Represents emergency contacts for each user.



from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, default="000-000-0000")  # Set default phone number

    def __str__(self):
        return f"{self.name} ({self.email})"



# Alert Model: Represents an emergency alert sent by a user to their contacts.
class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')  # Link each alert to a user
    message = models.TextField()
    location = models.CharField(max_length=255)
    contacts = models.ManyToManyField(Contact, related_name='alerts')  # Many-to-many relation to Contact
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set when the alert is created

    def __str__(self):
        return f"Alert from {self.user.username} at {self.timestamp}"  # String representation of the alert
