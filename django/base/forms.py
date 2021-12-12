from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from base.models import Pdf,Post

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ("file_name","content",)

class TextForm(forms.Form):
    file_name = forms.CharField(label="ファイル名")
    content = forms.CharField(label="テキスト",widget=forms.Textarea)
    # limit = forms.IntegerField(label="表示件数:")
    # save_or_not = forms.IntegerField(label="save or not save:")


#バリデーション
    # def clean(self):
    #     data = super().clean()
    #     content = data["content"]
    #     if len(content) <= 5:
    #         raise ValidationError("5文字以下です")
    #     return data

    def save(self):
        data = self.cleaned_data
        post = Pdf(file_name=data['file_name'], content=data['content'])
        post.save()

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