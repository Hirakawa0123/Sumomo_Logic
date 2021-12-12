from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from base.models import Pdf,Post

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

class TestForm(forms.Form):
    title = CharField(
        initial='',
        label='タイトル',
        max_length=10,
        required=True,  # 必須
    )
    comment = CharField(
        initial='',
        label='コメント',
        max_length=100,
        required=True,  # 必須
    )

    def save(self):
        # save data using the self.cleaned_data dictionary
        data = self.cleaned_data
        post = Post(title=data['title'], comment=data['comment'])
        post.save()

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()