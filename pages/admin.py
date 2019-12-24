from django.contrib import admin
from pages.models import Topic, Page, Section


class SectionInline (admin.StackedInline):
	model = Section
	extra = 1

class TopicAdmin (admin.ModelAdmin):
	list_display = ['name', 'order']

class PageAdmin (admin.ModelAdmin):
	list_display = ['name', 'topic']
	inlines = [SectionInline]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Page, PageAdmin)
