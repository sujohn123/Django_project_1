# send_email/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(widget=forms.TextInput(), required=True)