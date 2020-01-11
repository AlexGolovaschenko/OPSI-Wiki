from django.contrib import admin
from django.db import models
from django.forms import Textarea
from pages.models import Topic, Page, Section, Category, Reference, Link, File



class CategoryAdmin (admin.ModelAdmin):
	list_display = ['name', 'order']

class TopicAdmin (admin.ModelAdmin):
	list_display = ['name', 'order']

class SectionInline (admin.StackedInline):
	model = Section
	extra = 1

class FileInline (admin.TabularInline):
	model = File
	extra = 1

class LinkInline (admin.TabularInline):
	model = Link
	extra = 1
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

class ReferenceInline (admin.TabularInline):
	model = Reference
	extra = 1
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

class PageAdmin (admin.ModelAdmin):
	list_display = ['name', 'category', 'topic']
	inlines = [SectionInline, FileInline, LinkInline, ReferenceInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Page, PageAdmin)
