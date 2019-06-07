from django import forms
from .models import Profile, Statement

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profilepic','prefname', 'contact')

class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ('month','statement')