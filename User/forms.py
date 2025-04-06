from django import forms
from .models import UserType

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = ['usertype']
