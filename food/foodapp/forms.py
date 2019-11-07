from django import forms
from foodapp.models import *

class Form_name(forms.Form):
    name=forms.CharField(max_length=100,label="Name : ")
    emailId=forms.EmailField(max_length=40,required=True)
    password=forms.CharField(max_length=30,min_length=4,widget=forms.PasswordInput)
    phno=forms.CharField(min_length=10,max_length=10)
    Gender=forms.ChoiceField(choices=(('Male','Male'),('Female','Female')),widget=forms.RadioSelect)

class loginform(forms.Form):
    emailId=forms.EmailField(max_length=40,required=True)
    password=forms.CharField(max_length=30,min_length=4,widget=forms.PasswordInput)