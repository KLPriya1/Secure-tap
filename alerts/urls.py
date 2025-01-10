from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Add this import

urlpatterns = [
    path('send-alert/', views.send_alert, name='send_alert'),
    path('success/', views.alert_success, name='alert_success'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('user-alerts/', views.user_alerts, name='user_alerts'),
    path('signup/', views.signup, name='signup'),  # Add signup URL pattern

    path('login/', auth_views.LoginView.as_view(template_name='alerts/login.html'), name='login'),  # Custom login template
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]

