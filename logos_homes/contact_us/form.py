
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django import forms
from .models import Contacts


class ContactForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "uk-input uk-margin", "type": "text",
                                                         "placeholder": "Full Name", "required": "required"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "uk-input uk-margin", "type": "email",
                                                         "placeholder": "Email", "required": "required"}))
    contact_number = forms.CharField(widget=forms.NumberInput(attrs={"class": "uk-input uk-margin", "type": "text",
                                                                     "placeholder": "Phone Number", "required": "required"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "uk-textare uk-margin", "rows": "8",
                                                           "placeholder": "How can we help you?"}))

    def clean_name(self):
        name_passed = self.cleaned_data.get("name")
        if " " not in name_passed:
            raise ValidationError("Not a valid name, please enter your full name")
        else:
            return name_passed

    def validate_number(self, number):
        if str(number)[:3] == "+64":
            return True
        elif str(number)[:1] == "0":
            return True
        else:
            return False

    def clean_number(self):
        number_passed = self.cleaned_data.get("contact_number")
        if self.validate_number(number_passed):
            return number_passed
        else:
            raise ValidationError("Not a valid number")