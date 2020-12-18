from django import forms
from .models import *


class SheqForm(forms.ModelForm):
    what_you_saw = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'What did you see?'}), label='')
    reasons = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Reasons'}), label='')
    what_you_did = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'What you did to ensure you care?'}), label='')
    class Meta:
        model = t_sheq
        fields = ["rootid", "location", "what_you_saw", "reasons", "behavior", "possible_results", "what_you_did", "user"]