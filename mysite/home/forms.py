from django import forms
from .models import Student



class helpForm(forms.Form):

	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
	issue = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Issue'}))
	student_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Student ID'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}))
	number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Student ID'}))
	passcode = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Passcode'}))
	
	
	
class taLogin(forms.Form):
	student_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Student ID'}))
	passcode = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Passcode'}))