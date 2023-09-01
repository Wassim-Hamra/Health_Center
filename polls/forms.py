from django import forms
from django.core import validators
from polls.models import Visitor


def check_email(value):
    value = value.split('@')[-1]
    value = value.split('.')[0]
    providers = [
        "gmail",
        "yahoo",
        "outlook",
        "icloud",
        "aol",
        "protonmail",
        "zoho",
        "mail",
        "gmx",
        "yandex",
        "fastmail",
        "tutanota",
        "mail",
        "hushmail",
        "icloud",
        "mailinator",
        "comcast",
        "verizon",
        "att",
        "hotmail",
    ]
    if not (value in providers):
        raise forms.ValidationError("email provider not registered")


class Message(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'type': 'text', 'id': 'fname' ,'placeholder':"First Name"}))
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'placeholder':"Last Name",'type': 'text', 'class': 'form-control', 'id': 'lname'})
    )
    email = forms.EmailField(validators=[check_email],
                             widget=forms.EmailInput(attrs={'type':'email','class': 'form-control', 'id': 'email','placeholder':'Your Email'}))
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = Visitor
        fields = '__all__'
        widgets = {
            "message": forms.Textarea(
                attrs={'class': 'form-control', 'id':'message','placeholder': 'Your Message', 'rows': 5})
        }
