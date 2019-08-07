from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'cols': 80, 'placeholder': 'Title'}))
    text = forms.CharField(required=False,
                           widget=forms.Textarea(
                               attrs={
                                   'placeholder': 'Text',
                                   'rows': 15,
                                   'cols': 80
                               })
                           )

    class Meta:
        model = Article
        fields = {
            'title',
            'text'
        }
