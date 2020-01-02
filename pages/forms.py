from django import forms
from pages.models import Page, Section



class PageCreateForm (forms.ModelForm):
    class Meta:
        model = Page
        fields = ['category', 'topic', 'name', 'short_description']
 