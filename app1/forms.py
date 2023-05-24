from django import forms
from django.core.exceptions import ValidationError
from .models import contactModels

class contactForm(forms.ModelForm):
    class Meta:
        model = contactModels
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your name','required':'true'}),

            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Your Email','required':'true'}),
            'subject': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subject','required':'true'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder':'Message','rows':"5",'required':'true'})
        }
