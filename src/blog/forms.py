from django import forms
from .models import  Article


class Blogpost(forms.ModelForm):
    # title = forms.CharField(max_length=120)
    # content = forms.CharField()

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]