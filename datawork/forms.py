from django import forms
from datawork.models import *
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = "__all__"


class StudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(help_text="enter your email")
    
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")
    
