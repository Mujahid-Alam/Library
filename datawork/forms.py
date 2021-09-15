from django import forms
from django.forms.fields import IntegerField
from datawork.models import *
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ('title','author','language','no_of_page','edition','rent_price','isbn')


        

class StudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(help_text="enter your email")
    
    
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")


class UserCodeForm(forms.ModelForm):
    class Meta:
        model = UserCode
        exclude = ("user_id",)
    
