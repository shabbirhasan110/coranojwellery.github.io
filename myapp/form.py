from django import forms
from django.contrib.auth.forms import (UserCreationForm,AuthenticationForm,
UserChangeForm, PasswordChangeForm,PasswordResetForm,SetPasswordForm,PasswordResetForm,SetPasswordForm)
from .models import CustomerModel
from django.contrib.auth.models import User


# User Signup
class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),
            # 'first_name':forms.TextInput(attrs={'class':'form-control'}),
            # 'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Email'}),
        }

    def clean_email(self):
        em = self.cleaned_data['email']
        if em == '':
            raise forms.ValidationError('This field is required.')
        else:
            return em

# User Signin
class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','password']

class UserProfileChangeForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {

        'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),

        'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name'}),

        'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name'}),

        'email':forms.TextInput(attrs={'placeholder':'Enter E-Mail'}),

    }


class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Old Password'}))
    new_password1 =forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter New Password'}))
    new_password2 =forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Re-New Password'}))


# Customer Details For Address

city = (('Ahemdabad','Ahemdabad'),)
state = (('Gujarat','Gujarat'),)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['name','mobile','email','locality','zipcode','city','state']

        widgets = {
            # 'user':forms.TextInput(attrs={'class':'form-control','readonly':True}),
            'name':forms.TextInput(attrs={'placeholder':'Enter Name'}),
            'mobile':forms.NumberInput(attrs={'placeholder':'Enter Mobile Number'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter E-Mail'}),
            'locality':forms.TextInput(attrs={'placeholder':'Enter Address'}),
            'city':forms.Select(choices=city,attrs={'class':'nice-select'}),
            'zipcode':forms.TextInput(attrs={'placeholder':'Enter Zip-Code',}),
            'state':forms.Select(choices=state,attrs={'class':'mt-3 mb-3 nice-select'}),
        }

# Password Reset TextBox With Registred E-Mail
class PassResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Registered E-Mail'}))
    
# New Password Set Registred E-Mail Link
class SetNewPassForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm New Password'}))

