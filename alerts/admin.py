from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact, Alert

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'user')  # Customize the columns displayed

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('message', 'location', 'timestamp', 'user')  # Customize the columns displayed
