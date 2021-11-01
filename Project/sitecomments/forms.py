from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import SiteComments


class SiteCommentForm(forms.ModelForm):
    
    class Meta:
        model = SiteComments
        fields = ['name','email','comment']
