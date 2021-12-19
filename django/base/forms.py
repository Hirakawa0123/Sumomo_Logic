from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from base.models import Pdf,Search

class TextForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = (
            'file_name',
            'content',
        )
        widgets = {
            'content': forms.Textarea(attrs={'rows':15, 'cols':100})
        }

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class SearchQueryForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = (
            "search_name",
            "file_path",
            "search_query",
        )
        widgets = {
            "file_path": forms.Textarea(attrs={'rows':1, 'cols':100}),
            'search_query': forms.Textarea(attrs={'rows':15, 'cols':100})
        }