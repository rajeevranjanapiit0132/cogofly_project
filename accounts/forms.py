from django import forms 
from django.contrib.auth.forms import AuthenticationForm

from allauth.account.forms import SignupForm, LoginForm


class UserAuthForm(LoginForm):

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields["login"].widget = forms.EmailInput(
            attrs={
                "class": "input-text",
                "placeholder": "Email Address",
            }
        )
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "class": "input-text",
                "placeholder": "Password" 
            }
        )
        self.fields["remember"].widget = forms.CheckboxInput(
            attrs={
                "class": "form-check-input"
            }
        )

    def login(self, *args, **kwargs):
        return super().login(*args, **kwargs) 


class RegisterForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "class": "input-text",
                "placeholder": "Email Address" 
            }
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "input-text",
                "placeholder": "Choose Password" 
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "input-text",
                "placeholder": "Confirm Password" 
            }
        )

    first_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                "class": "input-text",
                "placeholder": "First Name",
            }
        )
    )
    last_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                "class": "input-text",
                "placeholder": "Last Name", 
            }
        )
    )
    
    def save(self, request):
        user = super().save(request) 
        user.is_traveller = True 
        user.save() 
        return user 
