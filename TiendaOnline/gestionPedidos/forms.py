from django import forms

class Contact_Form(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()