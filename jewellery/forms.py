from django import forms
from django.forms import ModelForm

class ProfileForm(forms.Form):
   #name = forms.CharField(max_length = 100)
   picture = forms.ImageField()
