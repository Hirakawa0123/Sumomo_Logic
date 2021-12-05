from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from base.models import Pdf

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ("file_name","content",)

class TextForm(forms.Form):
    text = forms.CharField(label="",widget=forms.Textarea)

    def clean(self):
        data = super().clean()
        text = data["text"]
        if len(text) <= 5:
            raise ValidationError("5文字以下です")
        return data
