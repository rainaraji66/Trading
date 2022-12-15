from django import forms
from django.utils import timezone


class uploadform(forms.Form):
    file = forms.FileField()