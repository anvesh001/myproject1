from django import forms

from .models import ExtractModel
from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import ExtractModel2

class ExtractForm(ModelForm):
    class Meta:
        model=ExtractModel
        fields=['cname','email','phone','requirements']

class ExtractForm2(ModelForm):
    class Meta:
        model=ExtractModel2
        fields=['cname','email','phone','requirements']
