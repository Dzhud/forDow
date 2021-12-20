from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import ugettext, ugettext_lazy as _
#from django.contrib.auth.models import User

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    country_code = forms.IntegerField()
    #role = forms.IntegerField()
    
    role = [(1,'Admin'),(2,'Team Member'),(3,'Freelancer'),(4,'Client'),(5,'Vendor'),(6,'Guest')]
    role = forms.CharField(label='Role', widget=forms.RadioSelect(choices=role))
    
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number =  forms.CharField(validators = [phoneNumberRegex], max_length = 20)
    
   
    
class UserLoginForm(forms.Form):
    user_name = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
    

class ImageLoginForm(forms.Form):
    files = forms.ImageField()