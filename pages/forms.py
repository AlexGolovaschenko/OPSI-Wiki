from django import forms
from django import template
from django.shortcuts import render
from ckeditor.widgets import CKEditorWidget
from pages.models import Page, Section, File, Link, Reference


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


SectionInlineFormSet = forms.inlineformset_factory(Page, Section, form=SectionCreateForm, 
	can_delete=True, extra = 0 )
 

class FileUploadForm (forms.ModelForm):
	upload = forms.FileField(required=False, widget=forms.FileInput( attrs={} ))
	comment = forms.CharField(max_length=200, required=False, 
		widget=forms.TextInput( attrs={'style': 'width:calc(100% - 110px);' } ))

	class Meta:
		model = File
		fields = ['upload', 'comment']

FileInlineFormSet = forms.inlineformset_factory(Page, File, form=FileUploadForm, 
	can_delete=True, extra = 0 )


class LinkCreateForm (forms.ModelForm):
	name = forms.CharField(max_length=200, required=False,
		widget=forms.TextInput( attrs={'style': 'width:calc(100% - 70px);' } ))
	link = forms.CharField(required=False, 
		widget=forms.TextInput( attrs={'style': 'width:calc(100% - 70px);' } ))

	class Meta:
		model = Link
		fields = ['name', 'link']

LinkInlineFormSet = forms.inlineformset_factory(Page, Link, form=LinkCreateForm, 
	can_delete=True, extra = 0 )


class ReferenceCreateForm (forms.ModelForm):
	name = forms.CharField(max_length=200, required=False,
		widget=forms.TextInput( attrs={'style': 'width:100%;' } ))
	link = forms.CharField(required=False, 
		widget=forms.TextInput( attrs={'style': 'width:100%;' } ))
	author = forms.CharField(max_length=200, required=False, 
		widget=forms.TextInput( attrs={'style': 'width:100%;' } ))
	pub_date = forms.CharField(max_length=200, required=False, 
		widget=forms.TextInput( attrs={'style': 'width:100%;' } ))

	class Meta:
		model = Reference
		fields = ['name', 'link', 'author', 'pub_date']

ReferenceInlineFormSet = forms.inlineformset_factory(Page, Reference, form=ReferenceCreateForm, 
	can_delete=True, extra = 0 )