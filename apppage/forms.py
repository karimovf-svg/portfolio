from django import forms
from apppage import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        fields = "__all__"