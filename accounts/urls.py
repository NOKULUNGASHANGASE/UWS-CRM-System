from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
# from accounts.forms import  MyPasswordResetForm, MySetPasswordForm
from . import views

urlpatterns = [
    # Registration and Login
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile Management
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    
    # Password Change (for logged-in users)
    path('password-change/', views.password_change_view, name='password_change'),
    
    # Password Reset (for users who forgot password)
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'), 
         name='reset_password'),

    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), 
     name='password_reset_confirm'),

    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'), 
         name='reset_password_complete'),
]