from django import forms
from django import template
from django.shortcuts import render
from ckeditor.widgets import CKEditorWidget
from pages.models import Page, Section


class PageCreateForm (forms.ModelForm):
	class Meta:
		model = Page
		fields = ['category', 'topic', 'name', 'short_description']
 

class SectionCreateForm (forms.ModelForm):
	headline = forms.CharField(max_length=200, required=False, label='Оглавление раздела')
	content = forms.CharField(widget=CKEditorWidget(), required=False, label='Раздел')

	class Meta:
		model = Section
		fields = ['headline', 'content']


def getSectionInlineFormSet (can_delete=False):
	return forms.inlineformset_factory(
		Page,
		Section, 
		form=SectionCreateForm, 
		can_delete=can_delete,
		extra = 0)

