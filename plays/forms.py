from django import forms
from .models import Show


class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['play', 'starts_at', 'actors']
        widgets = {
            'actors': forms.CheckboxSelectMultiple,
        }