from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
       
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # Add CSS classes to form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field_name].label
            })
    
    def clean_email(self):
        """Validate that email is unique"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['company','designation', 'phone_number', 'location', 'website']
            widgets = {
                
                'company': forms.TextInput(attrs={'class': 'form-control'}),
                'designation': forms.TextInput(attrs={'class': 'form-control'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
                'location': forms.TextInput(attrs={'class': 'form-control'}),
                'website': forms.URLInput(attrs={'class': 'form-control'}),
                # 'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            }

# class CustomPasswordResetForm(PasswordResetForm):
#     email = forms.EmailField(
#         max_length=254,
#         widget=forms.EmailInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your registered email',
#             }
#         )
#     )

# password reset
# class MyPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus ': 'True', 'autocomplete':'current-password', 'class':'form-control'}))
#     new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autofocus ': 'True', 'autocomplete':'current-password', 'class':'form-control'}))
#     new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autofocus ': 'True', 'autocomplete':'current-password', 'class':'form-control'}))
    
# class MyPasswordResetForm(PasswordResetForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


# class MySetPasswordForm(SetPasswordForm):
#     new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
#     new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
  