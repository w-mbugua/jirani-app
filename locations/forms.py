from django import forms
from .models import Contact,Business

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('owner',)