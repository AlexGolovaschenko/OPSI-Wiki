from django.contrib import admin
from django.db import models
from django.forms import Textarea
from pages.models import Topic, Page, Section, Category, Reference, Link



class CategoryAdmin (admin.ModelAdmin):
	list_display = ['name', 'order']

class TopicAdmin (admin.ModelAdmin):
	list_display = ['name', 'order']

class SectionInline (admin.StackedInline):
	model = Section
	extra = 0

class LinkInline (admin.TabularInline):
	model = Link
	extra = 0
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }

class ReferenceInline (admin.TabularInline):
	model = Reference
	extra = 0
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }

class PageAdmin (admin.ModelAdmin):
	list_display = ['name', 'category', 'topic']
	inlines = [SectionInline, LinkInline, ReferenceInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Page, PageAdmin)
