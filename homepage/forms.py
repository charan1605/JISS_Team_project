from .models import registrar,judge,lawyer
from django import forms

class getregistrar(forms.ModelForm):
    
    class Meta:
        model = registrar
        fields = ['username','password']

class getjudge(forms.ModelForm):
    
    class Meta:
        model = judge
        fields = ['username','password']


class getlawyer(forms.ModelForm):
    
    class Meta:
        model = lawyer
        fields = ['username','password']

