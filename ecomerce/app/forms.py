from django import forms
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    
    




class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-signin'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional validation logic if needed
        return cleaned_data
