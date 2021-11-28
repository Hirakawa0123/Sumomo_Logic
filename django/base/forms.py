from django import forms
from base.models import Pdf

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ("file_name", )