from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from shop_app.models import Customer

class customUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))

    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email id'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter password'}))

    class Meta:
       
        model = User
        fields = ['username','firstname','lastname','email','password1','password2']
    def __str__(self):
        return(self.username,self.firstname,self.lastname) 

class userprofile(forms.ModelForm):

    class Meta():
        model = Customer
        fields =('phone',)



            
        

